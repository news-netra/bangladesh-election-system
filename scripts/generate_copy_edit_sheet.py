#!/usr/bin/env python3
"""Build the editor-facing copy sheet from index.html and dynamic copy slots."""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
OUTPUT = ROOT / "copy-edit-sheet.md"

TOKEN_BY_ELEMENT_ID = {
    "legend-pool-count": "pool_count",
    "count-pool": "pool_count",
    "count-any": "countries_with_any",
    "count-pr": "pr_count",
    "count-after-pr": "after_pr",
    "count-pres-next": "president_count",
    "count-after-pres": "after_president",
    "count-second-next": "second_chamber_count",
    "count-after-second": "after_second_chamber",
}


def clean(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"\s+([,.;:!?])", r"\1", value)
    return value


def render_node(node, editable: bool) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    classes = set(node.get("class", []))
    if "swatch" in classes or "prviz-swatch" in classes or "prviz-arrow" in classes:
        return ""
    token = TOKEN_BY_ELEMENT_ID.get(node.get("id", ""))
    if editable and token:
        return "{" + token + "}"
    content = "".join(render_node(child, editable) for child in node.children)
    if node.name == "strong":
        return f"**{clean(content)}**"
    if node.name == "em":
        return f"*{clean(content)}*"
    if node.name == "a":
        return f"[{clean(content)}]({node.get('href', '')})"
    if editable and node.name == "span" and "n" in classes:
        return f"**{clean(content)}**"
    return content


def render_element(element: Tag, editable: bool) -> str:
    return clean("".join(render_node(child, editable) for child in element.children))


def dynamic(copy_id: str, current: str, locator: str, editable: str | None = None) -> dict:
    return {
        "id": copy_id,
        "current": current,
        "editable": editable if editable is not None else current,
        "locator": locator,
    }


DYNAMIC_FIELDS = [
    dynamic("BES.opening.legend.comparison.title", "Comparison set", "index.html :: applyStep() legend-title"),
    dynamic("BES.opening.legend.sieve.title.start", "Sieve begins", "index.html :: applyStep() legend-title"),
    dynamic("BES.opening.legend.sieve.title.found", "First safeguard found", "index.html :: applyStep() legend-title"),
    dynamic("BES.opening.legend.sieve.title.present", "Safeguards present", "index.html :: applyStep() legend-title"),
    dynamic("BES.opening.legend.sieve.title.example", "Example · Peru", "index.html :: applyStep() legend-title example template", "Example · {country}"),
    dynamic("BES.opening.legend.sieve.proportional.count", "PR · 32", "index.html :: applyStep() legend-prop-text", "PR · {pr_count}"),
    dynamic("BES.opening.legend.sieve.proportional.full", "Proportional seats", "index.html :: applyStep() legend-prop-text final"),
    dynamic("BES.opening.legend.sieve.proportional.short", "PR seats", "index.html :: applyStep() legend-prop-text compact"),
    dynamic("BES.opening.legend.sieve.president.count", "President adds · 9", "index.html :: applyStep() legend-pres-text", "President adds · {president_count}"),
    dynamic("BES.opening.legend.sieve.president.full", "Directly elected president", "index.html :: applyStep() legend-pres-text final"),
    dynamic("BES.opening.legend.sieve.president.short", "President", "index.html :: applyStep() legend-pres-text compact"),
    dynamic("BES.opening.legend.sieve.second-chamber.count", "Second chamber adds · 5", "index.html :: applyStep() legend-second-text", "Second chamber adds · {second_chamber_count}"),
    dynamic("BES.opening.legend.sieve.second-chamber.full", "Second chamber", "index.html :: applyStep() legend-second-text final"),
    dynamic("BES.opening.legend.sieve.second-chamber.short", "2nd chamber", "index.html :: applyStep() legend-second-text compact"),
    dynamic("BES.opening.legend.sieve.remainder", "Still in · 47", "index.html :: applyStep() legend-remainder-text", "Still in · {remaining_count}"),
    dynamic("BES.opening.legend.sieve.none-full", "None of the three · 1", "index.html :: applyStep() legend-none-text"),
    dynamic("BES.opening.legend.sieve.none-short", "None · 1", "index.html :: applyStep() legend-none-text compact"),
    dynamic("BES.opening.tally.comparison", "In the comparison", "index.html :: applyStep() tally comparison"),
    dynamic("BES.opening.tally.enter-sieve", "Enter the sieve", "index.html :: applyStep() tally sieve start"),
    dynamic("BES.opening.tally.without-pr", "Without PR", "index.html :: applyStep() tally proportional"),
    dynamic("BES.opening.tally.still-uncovered", "Still uncovered", "index.html :: applyStep() tally presidency/second chamber"),
    dynamic("BES.opening.tally.bangladesh", "Bangladesh", "index.html :: applyStep() tally reveal"),
    dynamic("BES.opening.example.peru.caption", "Lower-house PR", "index.html :: STEPS Peru caption"),
    dynamic("BES.opening.example.ghana.caption", "Elected executive president", "index.html :: STEPS Ghana caption"),
    dynamic("BES.opening.example.australia.caption", "Territorial second chamber", "index.html :: STEPS Australia caption"),
    dynamic("BES.opening.matrix.header.proportional", "PR seats", "index.html :: CORRECTIVES prop short"),
    dynamic("BES.opening.matrix.header.president", "President", "index.html :: CORRECTIVES pres short"),
    dynamic("BES.opening.matrix.header.second-chamber", "2nd chamber", "index.html :: CORRECTIVES second short"),
    dynamic("BES.opening.matrix.header.proportional-compact", "PR", "index.html :: build() compact matrix header"),
    dynamic("BES.opening.matrix.header.president-compact", "Pres.", "index.html :: build() compact matrix header"),
    dynamic("BES.opening.matrix.header.second-chamber-compact", "2nd", "index.html :: build() compact matrix header"),
    dynamic("BES.opening.matrix.none", "NO", "index.html :: build() Bangladesh matrix cells"),
    dynamic("BES.opening.map.bangladesh-label", "Bangladesh", "index.html :: computeGeo() map label"),
    dynamic("BES.opening.tooltip.lower-house-template", "{freedom_house_status} · Lower house: {electoral_system}", "index.html :: showTip() subline"),
    dynamic("BES.opening.tooltip.not-recorded", "not recorded", "index.html :: showTip() missing-system fallback"),
    dynamic("BES.opening.tooltip.yes", "YES", "index.html :: showTip() safeguard state"),
    dynamic("BES.opening.tooltip.no", "NO", "index.html :: showTip() safeguard state"),
    dynamic("BES.opening.tooltip.row.proportional", "Proportional seats", "index.html :: showTip() proportional row"),
    dynamic("BES.opening.tooltip.row.president", "Directly elected president", "index.html :: showTip() president row"),
    dynamic("BES.opening.tooltip.row.second-chamber", "Second chamber", "index.html :: showTip() second-chamber row"),
    dynamic("BES.opening.tooltip.status.enter", "Enters the three-safeguard sieve", "index.html :: sieveStatus() start"),
    dynamic("BES.opening.tooltip.status.first-found", "First safeguard found: Proportional seats", "index.html :: sieveStatus() first-found template", "First safeguard found: {safeguard}"),
    dynamic("BES.opening.tooltip.status.still-in", "Still in after the Proportional seats check", "index.html :: sieveStatus() still-in template", "Still in after the {safeguard} check"),
    dynamic("BES.opening.tooltip.status.final-none", "Final remaining country: none of the three", "index.html :: sieveStatus() final state"),
    dynamic("BES.opening.a11y.section", "How Bangladesh becomes an electoral outlier", "index.html :: #scrolly aria-label"),
    dynamic("BES.opening.a11y.visual", "World map and comparison matrix of electoral safeguards", "index.html :: #viz aria-label"),
    dynamic("BES.opening.a11y.legend", "Map legend", "index.html :: #legend aria-label"),
    dynamic("BES.opening.a11y.row-none", "Bangladesh: none of the three safeguards", "index.html :: build() matrix row aria-label"),
    dynamic("BES.opening.a11y.row-count", "Peru: 3 of 3 safeguards", "index.html :: build() matrix row aria-label template", "{country}: {safeguard_count} of 3 safeguards"),
    dynamic("BES.opening.a11y.sieve-enter", "Peru — enters the three-safeguard sieve", "index.html :: sieveAria() start template", "{country} — enters the three-safeguard sieve"),
    dynamic("BES.opening.a11y.sieve-first", "Peru — first safeguard found: Proportional seats", "index.html :: sieveAria() first-found template", "{country} — first safeguard found: {safeguard}"),
    dynamic("BES.opening.a11y.sieve-still", "Peru — still in after the Proportional seats check", "index.html :: sieveAria() still-in template", "{country} — still in after the {safeguard} check"),
    dynamic("BES.opening.a11y.sieve-final", "Bangladesh — final remaining country, none of the three safeguards", "index.html :: sieveAria() final template", "{country} — final remaining country, none of the three safeguards"),
    dynamic("BES.figure.vote.a11y.legend", "Vote-group colours", "index.html :: vote legend aria-label"),
    dynamic("BES.figure.vote.a11y.shift", "BNP share rises from 49.97 per cent to 53.04 per cent", "index.html :: .prviz-shift aria-label"),
    dynamic("BES.figure.vote.a11y.svg-title", "How excluding independent and rebel candidates changes the modeled vote shares", "index.html :: initVoteChart() SVG title"),
    dynamic("BES.figure.vote.a11y.svg-description", "BNP has 49.97 per cent of all valid votes and 53.04 per cent after 4.34 million independent and rebel votes are removed.", "index.html :: initVoteChart() SVG description"),
    dynamic("BES.figure.vote.row.all-valid", "All valid votes", "index.html :: initVoteChart() first row label"),
    dynamic("BES.figure.vote.row.modeled", "Votes admitted to the model", "index.html :: initVoteChart() second row label"),
    dynamic("BES.figure.vote.annotation.votes", "74.97m votes", "index.html :: initVoteChart() vote-total template", "{vote_total} votes"),
    dynamic("BES.figure.vote.annotation.excluded", "4.34m excluded", "index.html :: initVoteChart() excluded-vote template", "{excluded_votes} excluded"),
    dynamic("BES.figure.vote.ui.error", "Vote comparison could not load.", "index.html :: showError() vote chart"),
    dynamic("BES.figure.allocation.state.proposal.deck", "Illustrative BNP lower-house seat-share model.", "index.html :: states.proposal.deck and HTML fallback"),
    dynamic("BES.figure.allocation.state.proposal.summary", "BNP 72 · Jamaat 23 · all other parties 5", "index.html :: states.proposal.summary and HTML fallback"),
    dynamic("BES.figure.allocation.state.proposal.map-note", "The supplied files do not contain party wins by division for this seat-share model.", "index.html :: states.proposal.mapNote and HTML fallback"),
    dynamic("BES.figure.allocation.state.proposal.a11y-description", "Illustrative BNP seat-share proposal: BNP 72 seats, Jamaat 23, NCP 2, BKM 1 and other parties 2.", "index.html :: states.proposal.description"),
    dynamic("BES.figure.allocation.state.hare.deck", "Party votes · Hare quota · seats allocated within eight divisions.", "index.html :: states.hare.deck"),
    dynamic("BES.figure.allocation.state.hare.summary", "BNP 54 · Jamaat 35 · seven parties represented", "index.html :: states.hare.summary"),
    dynamic("BES.figure.allocation.state.hare.map-note", "No party majority in Barishal or Rangpur; Jamaat majority in Khulna.", "index.html :: states.hare.mapNote"),
    dynamic("BES.figure.allocation.state.hare.a11y-description", "Hare quota: BNP 54 seats, Jamaat 35, NCP 4, IAB 3, BKM 2, Islamic Front 1 and Khelafat Majlis 1.", "index.html :: states.hare.description"),
    dynamic("BES.figure.allocation.state.dhondt.deck", "The same party votes and divisions · D’Hondt allocation.", "index.html :: states.dhondt.deck"),
    dynamic("BES.figure.allocation.state.dhondt.summary", "BNP 61 · Jamaat 36 · five parties represented", "index.html :: states.dhondt.summary"),
    dynamic("BES.figure.allocation.state.dhondt.map-note", "BNP majority in seven divisions; Jamaat majority in Khulna.", "index.html :: states.dhondt.mapNote"),
    dynamic("BES.figure.allocation.state.dhondt.a11y-description", "D’Hondt: BNP 61 seats, Jamaat 36, NCP 1, IAB 1 and BKM 1.", "index.html :: states.dhondt.description"),
    dynamic("BES.figure.allocation.state.threshold.deck", "D’Hondt result with the two constitutional decision points.", "index.html :: states.threshold.deck"),
    dynamic("BES.figure.allocation.state.threshold.summary", "BNP clears 51 alone · no party reaches 67", "index.html :: states.threshold.summary"),
    dynamic("BES.figure.allocation.state.threshold.map-note", "The map is unchanged; the reference lines now show what the chamber can decide.", "index.html :: states.threshold.mapNote"),
    dynamic("BES.figure.allocation.state.threshold.a11y-description", "Under D’Hondt, BNP has 61 seats: above a 51-vote majority and below a two-thirds threshold of 67.", "index.html :: states.threshold.description"),
    dynamic("BES.figure.allocation.axis.simple-majority", "51 · simple majority", "index.html :: drawBar() first reference label"),
    dynamic("BES.figure.allocation.axis.two-thirds", "67 · two-thirds", "index.html :: drawBar() second reference label"),
    dynamic("BES.figure.allocation.axis.title", "Seats in a 100-seat chamber", "index.html :: drawBar() axis title"),
    dynamic("BES.figure.allocation.map.a11y.proposal-title", "Bangladesh divisions; no division allocation modelled", "index.html :: updateMap() proposal title"),
    dynamic("BES.figure.allocation.map.a11y.hare-title", "Division majorities under Hare quota", "index.html :: updateMap() Hare title"),
    dynamic("BES.figure.allocation.map.a11y.dhondt-title", "Division majorities under D’Hondt", "index.html :: updateMap() D’Hondt title"),
    dynamic("BES.figure.allocation.map.a11y.proposal-division", "Dhaka: division composition is not available for the illustrative seat-share model.", "index.html :: updateMap() proposal division template", "{division}: division composition is not available for the illustrative seat-share model."),
    dynamic("BES.figure.allocation.map.a11y.division", "Dhaka: BNP majority; BNP 15, Jamaat 8, NCP 1.", "index.html :: updateMap() modeled division template", "{division}: {majority_status}; {seat_composition}."),
    dynamic("BES.figure.allocation.ui.seat-error", "Seat comparison could not load.", "index.html :: allocation job error"),
    dynamic("BES.figure.allocation.ui.map-error", "Division map could not load.", "index.html :: allocation job error"),
    dynamic("BES.figure.allocation.ui.map-fallback", "The seat comparison remains available; the boundary file could not load.", "index.html :: initAllocationScrolly() map fallback"),
    dynamic("BES.label.party.bnp", "BNP", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.jamaat", "Jamaat", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.ncp", "NCP", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.iab", "IAB", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.bkm", "BKM", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.islamic-front", "Islamic Front", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.khelafat-majlis", "Khelafat Majlis", "index.html :: partyOrder/party legend display"),
    dynamic("BES.label.party.independent", "Independent candidates", "index.html :: party display label"),
    dynamic("BES.label.party.other", "Other parties", "index.html :: partyOrder/party legend display"),
]


GROUPS = [
    ("Page metadata and headline package", ("BES.meta.", "BES.story.category", "BES.story.headline", "BES.story.byline", "BES.story.standfirst")),
    ("Opening scrolly — narrative cards", ("BES.opening.card.",)),
    ("Opening scrolly — legends, examples and interface", ("BES.opening.legend.", "BES.opening.tally.", "BES.opening.example.", "BES.opening.matrix.", "BES.opening.map.", "BES.opening.ui.")),
    ("Opening scrolly — tooltip and accessibility copy", ("BES.opening.tooltip.", "BES.opening.a11y.")),
    ("Article body", ("BES.story.",)),
    ("Vote-denominator figure", ("BES.figure.vote.",)),
    ("Upper-house allocation figure", ("BES.figure.allocation.",)),
    ("Methodology", ("BES.methodology.",)),
    ("Party display labels", ("BES.label.party.",)),
]


def escape_cell(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def build_fields() -> list[dict]:
    soup = BeautifulSoup(INDEX.read_text(encoding="utf-8"), "html.parser")
    fields = []
    for element in soup.select("[data-copy-id]"):
        fields.append({
            "id": element["data-copy-id"],
            "current": render_element(element, editable=False),
            "editable": render_element(element, editable=True),
            "locator": f"index.html :: [data-copy-id=\"{element['data-copy-id']}\"]",
        })
    fields.extend(DYNAMIC_FIELDS)
    seen = set()
    duplicates = []
    for field in fields:
        if field["id"] in seen:
            duplicates.append(field["id"])
        seen.add(field["id"])
    if duplicates:
        raise RuntimeError(f"Duplicate tracking IDs: {', '.join(sorted(set(duplicates)))}")
    return fields


def group_for(copy_id: str) -> str:
    if copy_id.startswith("BES.story.") and copy_id not in {
        "BES.story.category", "BES.story.headline", "BES.story.byline", "BES.story.standfirst"
    }:
        return "Article body"
    for title, prefixes in GROUPS:
        if any(copy_id == prefix or copy_id.startswith(prefix) for prefix in prefixes):
            return title
    return "Other interface copy"


def build_markdown(fields: list[dict]) -> str:
    grouped = {title: [] for title, _ in GROUPS}
    grouped["Other interface copy"] = []
    for field in fields:
        grouped[group_for(field["id"])].append(field)

    lines = [
        "# Bangladesh election-system story — copy edit sheet",
        "",
        "Edit only the **Editable Markdown** column and keep every tracking ID unchanged. "
        "When finished, return this file to Codex; the IDs map each change back to the page.",
        "",
        "Protected placeholders such as `{pool_count}`, `{country}` and `{seat_composition}` are filled by the page. "
        "Keep them intact unless you want that live value removed from the sentence. Markdown links, `**bold**` and `*italics*` are supported.",
        "",
        "The sheet covers editorial copy, legends, chart states, tooltips and accessibility labels. "
        "Computed axis ticks, country/division names supplied directly by data, and numeric chart marks are intentionally excluded.",
        "",
    ]
    for title, _ in GROUPS + [("Other interface copy", ())]:
        items = grouped.get(title, [])
        if not items:
            continue
        lines.extend([f"## {title}", ""])
        for field in items:
            lines.extend([
                f"### `{field['id']}`",
                "",
                f"<!-- locator: {field['locator']} -->",
                "",
                "| Current version | Editable Markdown |",
                "| --- | --- |",
                f"| {escape_cell(field['current'])} | {escape_cell(field['editable'])} |",
                "",
            ])
    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    all_fields = build_fields()
    OUTPUT.write_text(build_markdown(all_fields), encoding="utf-8")
    print(f"Wrote {OUTPUT.name} with {len(all_fields)} tracked fields.")
