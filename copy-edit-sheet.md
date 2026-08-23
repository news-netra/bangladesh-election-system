# Bangladesh election-system story — copy edit sheet

Edit only the **Editable Markdown** column and keep every tracking ID unchanged. When finished, return this file to Codex; the IDs map each change back to the page.

Protected placeholders such as `{pool_count}`, `{country}` and `{seat_composition}` are filled by the page. Keep them intact unless you want that live value removed from the sentence. Markdown links, `**bold**` and `*italics*` are supported.

The sheet covers editorial copy, legends, chart states, tooltips and accessibility labels. Computed axis ticks, country/division names supplied directly by data, and numeric chart marks are intentionally excluded.

## Page metadata and headline package

### `BES.meta.page-title`

<!-- locator: index.html :: [data-copy-id="BES.meta.page-title"] -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh got the wrong kind of proportional representation — Netra News | Bangladesh got the wrong kind of proportional representation — Netra News |

### `BES.story.category`

<!-- locator: index.html :: [data-copy-id="BES.story.category"] -->

| Current version | Editable Markdown |
| --- | --- |
| Opinion | Opinion |

### `BES.story.headline`

<!-- locator: index.html :: [data-copy-id="BES.story.headline"] -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh, the world's most unchecked majoritarian democracy, needed proportional representation. It got the wrong kind. | Bangladesh, the world's most unchecked majoritarian democracy, needed proportional representation. It got the wrong kind. |

### `BES.story.byline`

<!-- locator: index.html :: [data-copy-id="BES.story.byline"] -->

| Current version | Editable Markdown |
| --- | --- |
| By Syed Ahlan Jadid and Nazmul Ahasan | By Syed Ahlan Jadid and Nazmul Ahasan |

### `BES.story.standfirst`

<!-- locator: index.html :: [data-copy-id="BES.story.standfirst"] -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh is debating a second chamber elected by proportional representation. It could become a counterweight to the lower-house majority — or a copy of it. The ballot, district, formula and decision rule decide which. | Bangladesh is debating a second chamber elected by proportional representation. It could become a counterweight to the lower-house majority — or a copy of it. The ballot, district, formula and decision rule decide which. |

## Opening scrolly — narrative cards

### `BES.opening.card.plurality`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.plurality"] -->

| Current version | Editable Markdown |
| --- | --- |
| Under FPTP, a plurality of votes can become a majority of seats. The larger question is whether that parliamentary majority becomes the only national power that matters. | Under FPTP, a plurality of votes can become a majority of seats. The larger question is whether that parliamentary majority becomes the only national power that matters. |

### `BES.opening.card.comparison-pool`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.comparison-pool"] -->

| Current version | Editable Markdown |
| --- | --- |
| To compare like with like, keep countries with at least 10 million people rated Free or Partly Free by Freedom House. 47 remain. | To compare like with like, keep countries with at least **10 million** people rated Free or Partly Free by Freedom House. {pool_count} remain. |

### `BES.opening.card.sieve-intro`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.sieve-intro"] -->

| Current version | Editable Markdown |
| --- | --- |
| Now run the 47 through three institutional arrangements that can disperse power. Once one appears, set that country aside; keep only those without any of the three. | Now run the 47 through three institutional arrangements that can disperse power. Once one appears, set that country aside; keep only those without any of the three. |

### `BES.opening.card.proportional`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.proportional"] -->

| Current version | Editable Markdown |
| --- | --- |
| Start inside parliament. 32 elect all or some lower-house seats through proportional rules. Set them aside. 15 still have no proportional component. | Start inside parliament. {pr_count} elect all or some lower-house seats through proportional rules. Set them aside. {after_pr} still have no proportional component. |

### `BES.opening.card.peru`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.peru"] -->

| Current version | Editable Markdown |
| --- | --- |
| Take Peru. Its 130 deputies are elected proportionally across 27 districts. Voters choose a party list and may name preferred candidates; seats are divided among lists rather than handed to one district winner. | Take Peru. Its **130** deputies are elected proportionally across **27** districts. Voters choose a party list and may name preferred candidates; seats are divided among lists rather than handed to one district winner. |

### `BES.opening.card.presidency`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.presidency"] -->

| Current version | Editable Markdown |
| --- | --- |
| Back across the comparison: of the 15 countries left, 9 directly elect a president. The office's power varies, but its mandate comes from voters, not parliament. 6 remain. | Back across the comparison: of the 15 countries left, {president_count} directly elect a president. The office's power varies, but its mandate comes from voters, not parliament. {after_president} remain. |

### `BES.opening.card.ghana`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.ghana"] -->

| Current version | Editable Markdown |
| --- | --- |
| Ghana shows what that separation means. Its MPs are elected one per constituency by FPTP. Voters separately choose the executive president nationwide; a winner needs more than 50%, or the top two face a runoff. | Ghana shows what that separation means. Its MPs are elected one per constituency by FPTP. Voters separately choose the executive president nationwide; a winner needs more than **50%**, or the top two face a runoff. |

### `BES.opening.card.second-chamber`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.second-chamber"] -->

| Current version | Editable Markdown |
| --- | --- |
| Six countries remain without proportional lower-house seats or a directly elected president. 5 have a second chamber, where legislation can be revised, delayed or stopped. 1 remains. | Six countries remain without proportional lower-house seats or a directly elected president. {second_chamber_count} have a second chamber, where legislation can be revised, delayed or stopped. {after_second_chamber} remains. |

### `BES.opening.card.australia`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.australia"] -->

| Current version | Editable Markdown |
| --- | --- |
| Take Australia. Every state elects 12 senators regardless of population; each mainland territory elects two. All bills need both houses, and the Senate can amend or reject most legislation—and refuse any bill. | Take Australia. Every state elects **12** senators regardless of population; each mainland territory elects two. All bills need both houses, and the Senate can amend or reject most legislation—and refuse any bill. |

### `BES.opening.card.bangladesh`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.bangladesh"] -->

| Current version | Editable Markdown |
| --- | --- |
| Across the full comparison, 46 have at least one of these arrangements. The last is Bangladesh: its general seats use FPTP, its president is not separately elected and it has no second chamber. Zero of three. | Across the full comparison, {countries_with_any} have at least one of these arrangements. The last is Bangladesh: its general seats use FPTP, its president is not separately elected and it has no second chamber. **Zero of three.** |

### `BES.opening.card.matrix`

<!-- locator: index.html :: [data-copy-id="BES.opening.card.matrix"] -->

| Current version | Editable Markdown |
| --- | --- |
| The matrix restores the overlaps: a country may have more than one safeguard. In this 47-country comparison, Bangladesh alone has three NOs. | The matrix restores the overlaps: a country may have more than one safeguard. In this 47-country comparison, Bangladesh alone has three NOs. |

## Opening scrolly — legends, examples and interface

### `BES.opening.legend.freedom-house.title`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.freedom-house.title"] -->

| Current version | Editable Markdown |
| --- | --- |
| Freedom House | Freedom House |

### `BES.opening.legend.freedom-house.free`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.freedom-house.free"] -->

| Current version | Editable Markdown |
| --- | --- |
| Free | Free |

### `BES.opening.legend.freedom-house.partly-free`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.freedom-house.partly-free"] -->

| Current version | Editable Markdown |
| --- | --- |
| Partly Free | Partly Free |

### `BES.opening.legend.freedom-house.not-free`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.freedom-house.not-free"] -->

| Current version | Editable Markdown |
| --- | --- |
| Not Free | Not Free |

### `BES.opening.legend.comparison.in`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.comparison.in"] -->

| Current version | Editable Markdown |
| --- | --- |
| In comparison · 47 | In comparison · {pool_count} |

### `BES.opening.legend.comparison.out`

<!-- locator: index.html :: [data-copy-id="BES.opening.legend.comparison.out"] -->

| Current version | Editable Markdown |
| --- | --- |
| Outside comparison | Outside comparison |

### `BES.opening.ui.scroll`

<!-- locator: index.html :: [data-copy-id="BES.opening.ui.scroll"] -->

| Current version | Editable Markdown |
| --- | --- |
| Scroll | Scroll |

### `BES.opening.legend.comparison.title`

<!-- locator: index.html :: applyStep() legend-title -->

| Current version | Editable Markdown |
| --- | --- |
| Comparison set | Comparison set |

### `BES.opening.legend.sieve.title.start`

<!-- locator: index.html :: applyStep() legend-title -->

| Current version | Editable Markdown |
| --- | --- |
| Sieve begins | Sieve begins |

### `BES.opening.legend.sieve.title.found`

<!-- locator: index.html :: applyStep() legend-title -->

| Current version | Editable Markdown |
| --- | --- |
| First safeguard found | First safeguard found |

### `BES.opening.legend.sieve.title.present`

<!-- locator: index.html :: applyStep() legend-title -->

| Current version | Editable Markdown |
| --- | --- |
| Safeguards present | Safeguards present |

### `BES.opening.legend.sieve.title.example`

<!-- locator: index.html :: applyStep() legend-title example template -->

| Current version | Editable Markdown |
| --- | --- |
| Example · Peru | Example · {country} |

### `BES.opening.legend.sieve.proportional.count`

<!-- locator: index.html :: applyStep() legend-prop-text -->

| Current version | Editable Markdown |
| --- | --- |
| PR · 32 | PR · {pr_count} |

### `BES.opening.legend.sieve.proportional.full`

<!-- locator: index.html :: applyStep() legend-prop-text final -->

| Current version | Editable Markdown |
| --- | --- |
| Proportional seats | Proportional seats |

### `BES.opening.legend.sieve.proportional.short`

<!-- locator: index.html :: applyStep() legend-prop-text compact -->

| Current version | Editable Markdown |
| --- | --- |
| PR seats | PR seats |

### `BES.opening.legend.sieve.president.count`

<!-- locator: index.html :: applyStep() legend-pres-text -->

| Current version | Editable Markdown |
| --- | --- |
| President adds · 9 | President adds · {president_count} |

### `BES.opening.legend.sieve.president.full`

<!-- locator: index.html :: applyStep() legend-pres-text final -->

| Current version | Editable Markdown |
| --- | --- |
| Directly elected president | Directly elected president |

### `BES.opening.legend.sieve.president.short`

<!-- locator: index.html :: applyStep() legend-pres-text compact -->

| Current version | Editable Markdown |
| --- | --- |
| President | President |

### `BES.opening.legend.sieve.second-chamber.count`

<!-- locator: index.html :: applyStep() legend-second-text -->

| Current version | Editable Markdown |
| --- | --- |
| Second chamber adds · 5 | Second chamber adds · {second_chamber_count} |

### `BES.opening.legend.sieve.second-chamber.full`

<!-- locator: index.html :: applyStep() legend-second-text final -->

| Current version | Editable Markdown |
| --- | --- |
| Second chamber | Second chamber |

### `BES.opening.legend.sieve.second-chamber.short`

<!-- locator: index.html :: applyStep() legend-second-text compact -->

| Current version | Editable Markdown |
| --- | --- |
| 2nd chamber | 2nd chamber |

### `BES.opening.legend.sieve.remainder`

<!-- locator: index.html :: applyStep() legend-remainder-text -->

| Current version | Editable Markdown |
| --- | --- |
| Still in · 47 | Still in · {remaining_count} |

### `BES.opening.legend.sieve.none-full`

<!-- locator: index.html :: applyStep() legend-none-text -->

| Current version | Editable Markdown |
| --- | --- |
| None of the three · 1 | None of the three · 1 |

### `BES.opening.legend.sieve.none-short`

<!-- locator: index.html :: applyStep() legend-none-text compact -->

| Current version | Editable Markdown |
| --- | --- |
| None · 1 | None · 1 |

### `BES.opening.tally.comparison`

<!-- locator: index.html :: applyStep() tally comparison -->

| Current version | Editable Markdown |
| --- | --- |
| In the comparison | In the comparison |

### `BES.opening.tally.enter-sieve`

<!-- locator: index.html :: applyStep() tally sieve start -->

| Current version | Editable Markdown |
| --- | --- |
| Enter the sieve | Enter the sieve |

### `BES.opening.tally.without-pr`

<!-- locator: index.html :: applyStep() tally proportional -->

| Current version | Editable Markdown |
| --- | --- |
| Without PR | Without PR |

### `BES.opening.tally.still-uncovered`

<!-- locator: index.html :: applyStep() tally presidency/second chamber -->

| Current version | Editable Markdown |
| --- | --- |
| Still uncovered | Still uncovered |

### `BES.opening.tally.bangladesh`

<!-- locator: index.html :: applyStep() tally reveal -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh | Bangladesh |

### `BES.opening.example.peru.caption`

<!-- locator: index.html :: STEPS Peru caption -->

| Current version | Editable Markdown |
| --- | --- |
| Lower-house PR | Lower-house PR |

### `BES.opening.example.ghana.caption`

<!-- locator: index.html :: STEPS Ghana caption -->

| Current version | Editable Markdown |
| --- | --- |
| Elected executive president | Elected executive president |

### `BES.opening.example.australia.caption`

<!-- locator: index.html :: STEPS Australia caption -->

| Current version | Editable Markdown |
| --- | --- |
| Territorial second chamber | Territorial second chamber |

### `BES.opening.matrix.header.proportional`

<!-- locator: index.html :: CORRECTIVES prop short -->

| Current version | Editable Markdown |
| --- | --- |
| PR seats | PR seats |

### `BES.opening.matrix.header.president`

<!-- locator: index.html :: CORRECTIVES pres short -->

| Current version | Editable Markdown |
| --- | --- |
| President | President |

### `BES.opening.matrix.header.second-chamber`

<!-- locator: index.html :: CORRECTIVES second short -->

| Current version | Editable Markdown |
| --- | --- |
| 2nd chamber | 2nd chamber |

### `BES.opening.matrix.header.proportional-compact`

<!-- locator: index.html :: build() compact matrix header -->

| Current version | Editable Markdown |
| --- | --- |
| PR | PR |

### `BES.opening.matrix.header.president-compact`

<!-- locator: index.html :: build() compact matrix header -->

| Current version | Editable Markdown |
| --- | --- |
| Pres. | Pres. |

### `BES.opening.matrix.header.second-chamber-compact`

<!-- locator: index.html :: build() compact matrix header -->

| Current version | Editable Markdown |
| --- | --- |
| 2nd | 2nd |

### `BES.opening.matrix.none`

<!-- locator: index.html :: build() Bangladesh matrix cells -->

| Current version | Editable Markdown |
| --- | --- |
| NO | NO |

### `BES.opening.map.bangladesh-label`

<!-- locator: index.html :: computeGeo() map label -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh | Bangladesh |

## Opening scrolly — tooltip and accessibility copy

### `BES.opening.tooltip.lower-house-template`

<!-- locator: index.html :: showTip() subline -->

| Current version | Editable Markdown |
| --- | --- |
| {freedom_house_status} · Lower house: {electoral_system} | {freedom_house_status} · Lower house: {electoral_system} |

### `BES.opening.tooltip.not-recorded`

<!-- locator: index.html :: showTip() missing-system fallback -->

| Current version | Editable Markdown |
| --- | --- |
| not recorded | not recorded |

### `BES.opening.tooltip.yes`

<!-- locator: index.html :: showTip() safeguard state -->

| Current version | Editable Markdown |
| --- | --- |
| YES | YES |

### `BES.opening.tooltip.no`

<!-- locator: index.html :: showTip() safeguard state -->

| Current version | Editable Markdown |
| --- | --- |
| NO | NO |

### `BES.opening.tooltip.row.proportional`

<!-- locator: index.html :: showTip() proportional row -->

| Current version | Editable Markdown |
| --- | --- |
| Proportional seats | Proportional seats |

### `BES.opening.tooltip.row.president`

<!-- locator: index.html :: showTip() president row -->

| Current version | Editable Markdown |
| --- | --- |
| Directly elected president | Directly elected president |

### `BES.opening.tooltip.row.second-chamber`

<!-- locator: index.html :: showTip() second-chamber row -->

| Current version | Editable Markdown |
| --- | --- |
| Second chamber | Second chamber |

### `BES.opening.tooltip.status.enter`

<!-- locator: index.html :: sieveStatus() start -->

| Current version | Editable Markdown |
| --- | --- |
| Enters the three-safeguard sieve | Enters the three-safeguard sieve |

### `BES.opening.tooltip.status.first-found`

<!-- locator: index.html :: sieveStatus() first-found template -->

| Current version | Editable Markdown |
| --- | --- |
| First safeguard found: Proportional seats | First safeguard found: {safeguard} |

### `BES.opening.tooltip.status.still-in`

<!-- locator: index.html :: sieveStatus() still-in template -->

| Current version | Editable Markdown |
| --- | --- |
| Still in after the Proportional seats check | Still in after the {safeguard} check |

### `BES.opening.tooltip.status.final-none`

<!-- locator: index.html :: sieveStatus() final state -->

| Current version | Editable Markdown |
| --- | --- |
| Final remaining country: none of the three | Final remaining country: none of the three |

### `BES.opening.a11y.section`

<!-- locator: index.html :: #scrolly aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| How Bangladesh becomes an electoral outlier | How Bangladesh becomes an electoral outlier |

### `BES.opening.a11y.visual`

<!-- locator: index.html :: #viz aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| World map and comparison matrix of electoral safeguards | World map and comparison matrix of electoral safeguards |

### `BES.opening.a11y.legend`

<!-- locator: index.html :: #legend aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| Map legend | Map legend |

### `BES.opening.a11y.row-none`

<!-- locator: index.html :: build() matrix row aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh: none of the three safeguards | Bangladesh: none of the three safeguards |

### `BES.opening.a11y.row-count`

<!-- locator: index.html :: build() matrix row aria-label template -->

| Current version | Editable Markdown |
| --- | --- |
| Peru: 3 of 3 safeguards | {country}: {safeguard_count} of 3 safeguards |

### `BES.opening.a11y.sieve-enter`

<!-- locator: index.html :: sieveAria() start template -->

| Current version | Editable Markdown |
| --- | --- |
| Peru — enters the three-safeguard sieve | {country} — enters the three-safeguard sieve |

### `BES.opening.a11y.sieve-first`

<!-- locator: index.html :: sieveAria() first-found template -->

| Current version | Editable Markdown |
| --- | --- |
| Peru — first safeguard found: Proportional seats | {country} — first safeguard found: {safeguard} |

### `BES.opening.a11y.sieve-still`

<!-- locator: index.html :: sieveAria() still-in template -->

| Current version | Editable Markdown |
| --- | --- |
| Peru — still in after the Proportional seats check | {country} — still in after the {safeguard} check |

### `BES.opening.a11y.sieve-final`

<!-- locator: index.html :: sieveAria() final template -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh — final remaining country, none of the three safeguards | {country} — final remaining country, none of the three safeguards |

## Article body

### `BES.story.intro.models`

<!-- locator: index.html :: [data-copy-id="BES.story.intro.models"] -->

| Current version | Editable Markdown |
| --- | --- |
| The July Charter proposes a bicameral parliament with an upper house elected through proportional representation. But the dispute contains two different models: use each party’s lower-house vote share to compose the upper house, or use the share of seats it won below — the model set out in the BNP’s note of dissent and manifesto. The supplied division file simulates the first. To illustrate the second below, we use the EC-declared party-held general seats. | The July Charter proposes a bicameral parliament with an upper house elected through proportional representation. But the dispute contains two different models: use each party’s lower-house vote share to compose the upper house, or use the share of seats it won below — the model set out in the BNP’s note of dissent and manifesto. The supplied division file simulates the first. To illustrate the second below, we use the EC-declared party-held general seats. |

### `BES.story.denominator.heading`

<!-- locator: index.html :: [data-copy-id="BES.story.denominator.heading"] -->

| Current version | Editable Markdown |
| --- | --- |
| The majority appears before the formula | The majority appears before the formula |

### `BES.story.denominator.exclusion`

<!-- locator: index.html :: [data-copy-id="BES.story.denominator.exclusion"] -->

| Current version | Editable Markdown |
| --- | --- |
| The supplied simulation starts with lower-house votes and excludes independent and rebel candidates because it models the upper house as a contest among party lists. That exclusion is one of the model’s most important limitations: those candidates drew more votes collectively than any party except BNP and Jamaat. | The supplied simulation starts with lower-house votes and excludes independent and rebel candidates because it models the upper house as a contest among party lists. That exclusion is one of the model’s most important limitations: those candidates drew more votes collectively than any party except BNP and Jamaat. |

### `BES.story.denominator.effect`

<!-- locator: index.html :: [data-copy-id="BES.story.denominator.effect"] -->

| Current version | Editable Markdown |
| --- | --- |
| In the supplied 2026 division totals, the excluded votes total **4,339,706**, or **5.79 per cent** of all valid votes. Once they are removed from the denominator, BNP moves from just below half of all valid votes to a majority of the votes admitted to the model. | In the supplied 2026 division totals, the excluded votes total **4,339,706**, or **5.79 per cent** of all valid votes. Once they are removed from the denominator, BNP moves from just below half of all valid votes to a majority of the votes admitted to the model. |

### `BES.story.allocation.heading`

<!-- locator: index.html :: [data-copy-id="BES.story.allocation.heading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Setting the rules decides who benefits | Setting the rules decides who benefits |

### `BES.story.allocation.charter-vs-bnp`

<!-- locator: index.html :: [data-copy-id="BES.story.allocation.charter-vs-bnp"] -->

| Current version | Editable Markdown |
| --- | --- |
| The July Charter promises a 100-seat upper house proportional to parties’ national lower-house votes. BNP’s note of dissent instead proposes carrying lower-house seat shares upstairs. Neither position settles the allocation formula, treatment of independent votes or geographic design — so neither produces a unique chamber on its own. | The July Charter promises a 100-seat upper house proportional to parties’ national lower-house votes. BNP’s note of dissent instead proposes carrying lower-house seat shares upstairs. Neither position settles the allocation formula, treatment of independent votes or geographic design — so neither produces a unique chamber on its own. |

### `BES.story.allocation.frame-guide`

<!-- locator: index.html :: [data-copy-id="BES.story.allocation.frame-guide"] -->

| Current version | Editable Markdown |
| --- | --- |
| The first frame below illustrates BNP’s seat-share model using party-held general seats. The next two hold the party-vote pool, eight divisional seat magnitudes and 100-seat total constant, changing only the allocation formula. | The first frame below illustrates BNP’s seat-share model using party-held general seats. The next two hold the party-vote pool, eight divisional seat magnitudes and 100-seat total constant, changing only the allocation formula. |

### `BES.story.geography.heading`

<!-- locator: index.html :: [data-copy-id="BES.story.geography.heading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Geography is another electoral rule | Geography is another electoral rule |

### `BES.story.geography.design`

<!-- locator: index.html :: [data-copy-id="BES.story.geography.design"] -->

| Current version | Editable Markdown |
| --- | --- |
| Much of the discussion treats Bangladesh as one national electoral district. The original analysis instead assigns the 100 seats to divisions by registered voters — six to Barishal, seven to Sylhet, 24 to Dhaka and between eight and 20 elsewhere — to preserve a geographic link. But those smaller district magnitudes also make it harder for smaller parties to win a seat. | Much of the discussion treats Bangladesh as one national electoral district. The original analysis instead assigns the 100 seats to divisions by registered voters — six to Barishal, seven to Sylhet, 24 to Dhaka and between eight and 20 elsewhere — to preserve a geographic link. But those smaller district magnitudes also make it harder for smaller parties to win a seat. |

### `BES.story.geography.results`

<!-- locator: index.html :: [data-copy-id="BES.story.geography.results"] -->

| Current version | Editable Markdown |
| --- | --- |
| In one national district, Hare would seat 10 parties and give BNP 53 seats; divided eight ways, it seats seven parties and gives BNP 54. National D’Hondt gives BNP 56 seats; division-by-division D’Hondt gives it 61. | In one national district, Hare would seat 10 parties and give BNP 53 seats; divided eight ways, it seats seven parties and gives BNP 54. National D’Hondt gives BNP 56 seats; division-by-division D’Hondt gives it 61. |

### `BES.story.scrutiny.heading`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.heading"] -->

| Current version | Editable Markdown |
| --- | --- |
| The rules still need scrutiny | The rules still need scrutiny |

### `BES.story.scrutiny.intro`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.intro"] -->

| Current version | Editable Markdown |
| --- | --- |
| The problem is not proportional representation itself. It is that every unresolved rule changes who is represented, who benefits, or how much power the largest party can exercise: which votes count, whether seats are allocated nationally or by division, which formula converts votes into seats, and what decisions require more than a simple majority. | The problem is not proportional representation itself. It is that every unresolved rule changes who is represented, who benefits, or how much power the largest party can exercise: which votes count, whether seats are allocated nationally or by division, which formula converts votes into seats, and what decisions require more than a simple majority. |

### `BES.story.scrutiny.votes`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.votes"] -->

| Current version | Editable Markdown |
| --- | --- |
| **First, lawmakers must decide which votes count.** A vote-based model can reuse lower-house constituency totals or ask voters for a separate upper-house party-list vote. Reusing the lower-house result excludes independent candidates from a party-only allocation and may not measure the same preference. | **First, lawmakers must decide which votes count.** A vote-based model can reuse lower-house constituency totals or ask voters for a separate upper-house party-list vote. Reusing the lower-house result excludes independent candidates from a party-only allocation and may not measure the same preference. |

### `BES.story.scrutiny.geography`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.geography"] -->

| Current version | Editable Markdown |
| --- | --- |
| **They must also decide how geography enters the allocation.** A national district is more proportional in this simulation but may concentrate nominees, while division lists preserve a regional link but make it harder for smaller parties to win seats. A national levelling tier could reconcile the two goals. | **They must also decide how geography enters the allocation.** A national district is more proportional in this simulation but may concentrate nominees, while division lists preserve a regional link but make it harder for smaller parties to win seats. A national levelling tier could reconcile the two goals. |

### `BES.story.scrutiny.formula`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.formula"] -->

| Current version | Editable Markdown |
| --- | --- |
| **Finally, the formula and decision rule must be set before the election.** Hare and D’Hondt produce different representation from the same votes; the chamber’s voting requirement then determines whether the largest party can act alone. | **Finally, the formula and decision rule must be set before the election.** Hare and D’Hondt produce different representation from the same votes; the chamber’s voting requirement then determines whether the largest party can act alone. |

### `BES.story.scrutiny.conclusion`

<!-- locator: index.html :: [data-copy-id="BES.story.scrutiny.conclusion"] -->

| Current version | Editable Markdown |
| --- | --- |
| The debate is therefore not simply PR or no PR. Setting the rules at the beginning will determine whose votes count, which parties gain representation and whether the second chamber becomes a counterweight or a mirror. | The debate is therefore not simply PR or no PR. Setting the rules at the beginning will determine whose votes count, which parties gain representation and whether the second chamber becomes a counterweight or a mirror. |

## Vote-denominator figure

### `BES.figure.vote.title`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.title"] -->

| Current version | Editable Markdown |
| --- | --- |
| Drop 4.34 million votes, and 49.97% becomes 53.04% | Drop 4.34 million votes, and 49.97% becomes 53.04% |

### `BES.figure.vote.deck`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.deck"] -->

| Current version | Editable Markdown |
| --- | --- |
| All valid lower-house votes compared with the party-only vote pool used in the upper-house simulation. | All valid lower-house votes compared with the party-only vote pool used in the upper-house simulation. |

### `BES.figure.vote.legend.bnp`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.legend.bnp"] -->

| Current version | Editable Markdown |
| --- | --- |
| BNP | BNP |

### `BES.figure.vote.legend.jamaat`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.legend.jamaat"] -->

| Current version | Editable Markdown |
| --- | --- |
| Jamaat | Jamaat |

### `BES.figure.vote.legend.independent`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.legend.independent"] -->

| Current version | Editable Markdown |
| --- | --- |
| Independent and rebel candidates | Independent and rebel candidates |

### `BES.figure.vote.legend.other`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.legend.other"] -->

| Current version | Editable Markdown |
| --- | --- |
| Other parties | Other parties |

### `BES.figure.vote.ui.loading`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.ui.loading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Loading vote comparison… | Loading vote comparison… |

### `BES.figure.vote.shift-note`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.shift-note"] -->

| Current version | Editable Markdown |
| --- | --- |
| BNP’s share after independent and rebel votes are excluded from the denominator | BNP’s share after independent and rebel votes are excluded from the denominator |

### `BES.figure.vote.caption`

<!-- locator: index.html :: [data-copy-id="BES.figure.vote.caption"] -->

| Current version | Editable Markdown |
| --- | --- |
| Source: supplied 2026 results by division; Netra calculation. Independent and rebel votes are excluded from the model. | Source: supplied 2026 results by division; Netra calculation. Independent and rebel votes are excluded from the model. |

### `BES.figure.vote.a11y.legend`

<!-- locator: index.html :: vote legend aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| Vote-group colours | Vote-group colours |

### `BES.figure.vote.a11y.shift`

<!-- locator: index.html :: .prviz-shift aria-label -->

| Current version | Editable Markdown |
| --- | --- |
| BNP share rises from 49.97 per cent to 53.04 per cent | BNP share rises from 49.97 per cent to 53.04 per cent |

### `BES.figure.vote.a11y.svg-title`

<!-- locator: index.html :: initVoteChart() SVG title -->

| Current version | Editable Markdown |
| --- | --- |
| How excluding independent and rebel candidates changes the modeled vote shares | How excluding independent and rebel candidates changes the modeled vote shares |

### `BES.figure.vote.a11y.svg-description`

<!-- locator: index.html :: initVoteChart() SVG description -->

| Current version | Editable Markdown |
| --- | --- |
| BNP has 49.97 per cent of all valid votes and 53.04 per cent after 4.34 million independent and rebel votes are removed. | BNP has 49.97 per cent of all valid votes and 53.04 per cent after 4.34 million independent and rebel votes are removed. |

### `BES.figure.vote.row.all-valid`

<!-- locator: index.html :: initVoteChart() first row label -->

| Current version | Editable Markdown |
| --- | --- |
| All valid votes | All valid votes |

### `BES.figure.vote.row.modeled`

<!-- locator: index.html :: initVoteChart() second row label -->

| Current version | Editable Markdown |
| --- | --- |
| Votes admitted to the model | Votes admitted to the model |

### `BES.figure.vote.annotation.votes`

<!-- locator: index.html :: initVoteChart() vote-total template -->

| Current version | Editable Markdown |
| --- | --- |
| 74.97m votes | {vote_total} votes |

### `BES.figure.vote.annotation.excluded`

<!-- locator: index.html :: initVoteChart() excluded-vote template -->

| Current version | Editable Markdown |
| --- | --- |
| 4.34m excluded | {excluded_votes} excluded |

### `BES.figure.vote.ui.error`

<!-- locator: index.html :: showError() vote chart -->

| Current version | Editable Markdown |
| --- | --- |
| Vote comparison could not load. | Vote comparison could not load. |

## Upper-house allocation figure

### `BES.figure.allocation.title`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.title"] -->

| Current version | Editable Markdown |
| --- | --- |
| One upper house, three very different outcomes | One upper house, three very different outcomes |

### `BES.figure.allocation.ui.seat-loading`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.ui.seat-loading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Loading seat comparison… | Loading seat comparison… |

### `BES.figure.allocation.map.legend.bnp-majority`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.map.legend.bnp-majority"] -->

| Current version | Editable Markdown |
| --- | --- |
| BNP majority | BNP majority |

### `BES.figure.allocation.map.legend.no-majority`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.map.legend.no-majority"] -->

| Current version | Editable Markdown |
| --- | --- |
| No party majority | No party majority |

### `BES.figure.allocation.map.legend.jamaat-majority`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.map.legend.jamaat-majority"] -->

| Current version | Editable Markdown |
| --- | --- |
| Jamaat majority | Jamaat majority |

### `BES.figure.allocation.ui.map-loading`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.ui.map-loading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Loading division map… | Loading division map… |

### `BES.figure.allocation.state.proposal.card`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.state.proposal.card"] -->

| Current version | Editable Markdown |
| --- | --- |
| Carry the lower house’s party-seat shares upstairs and the FPTP landslide is largely reproduced: an illustrative allocation gives BNP 72 seats, Jamaat 23, and every other party combined just 5. | Carry the lower house’s party-seat shares upstairs and the FPTP landslide is largely reproduced: an illustrative allocation gives BNP **72** seats, Jamaat **23**, and every other party combined just **5**. |

### `BES.figure.allocation.state.hare.card`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.state.hare.card"] -->

| Current version | Editable Markdown |
| --- | --- |
| Use party votes instead and apply Hare quota inside eight divisions. BNP falls to 54 seats, Jamaat rises to 35, and seven parties enter the chamber. Barishal and Rangpur have no single-party majority. | Use party votes instead and apply Hare quota inside eight divisions. BNP falls to **54** seats, Jamaat rises to **35**, and seven parties enter the chamber. Barishal and Rangpur have no single-party majority. |

### `BES.figure.allocation.state.dhondt.card`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.state.dhondt.card"] -->

| Current version | Editable Markdown |
| --- | --- |
| Keep those votes and divisions unchanged, but switch to D’Hondt. BNP climbs to 61 seats and Jamaat to 36. Only five parties remain; Islamic Front and Khelafat Majlis disappear. | Keep those votes and divisions unchanged, but switch to D’Hondt. BNP climbs to **61** seats and Jamaat to **36**. Only five parties remain; Islamic Front and Khelafat Majlis disappear. |

### `BES.figure.allocation.state.threshold.card`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.state.threshold.card"] -->

| Current version | Editable Markdown |
| --- | --- |
| The seat-share mirror puts BNP above even 67. Hare and D’Hondt still leave it above the 51 votes needed to act alone, but below two-thirds. The formula decides who enters the room; the voting rule decides what the largest party can do there. | The seat-share mirror puts BNP above even **67**. Hare and D’Hondt still leave it above the **51** votes needed to act alone, but below two-thirds. The formula decides who enters the room; the voting rule decides what the largest party can do there. |

### `BES.figure.allocation.caption`

<!-- locator: index.html :: [data-copy-id="BES.figure.allocation.caption"] -->

| Current version | Editable Markdown |
| --- | --- |
| Sources: [Election Commission referendum circular](https://www.ecs.gov.bd/files/oCo9rPBkcdilk9WlZFnYlcFALB8UDYtuYaCRFh4Q.pdf); [EC-declared general-seat results reported by BSS](https://www.bssnews.net/national-parlament-election-2026/360856); supplied 2026 division results; Netra calculations. The BNP seat-share frame is illustrative: party-held seats only, smaller one-seat parties grouped and Hare largest-remainder rounding. Boundary: [geoBoundaries gbOpen](https://www.geoboundaries.org/), BGD ADM1 (CC BY 4.0). | Sources: [Election Commission referendum circular](https://www.ecs.gov.bd/files/oCo9rPBkcdilk9WlZFnYlcFALB8UDYtuYaCRFh4Q.pdf); [EC-declared general-seat results reported by BSS](https://www.bssnews.net/national-parlament-election-2026/360856); supplied 2026 division results; Netra calculations. The BNP seat-share frame is illustrative: party-held seats only, smaller one-seat parties grouped and Hare largest-remainder rounding. Boundary: [geoBoundaries gbOpen](https://www.geoboundaries.org/), BGD ADM1 (CC BY 4.0). |

### `BES.figure.allocation.state.proposal.deck`

<!-- locator: index.html :: states.proposal.deck and HTML fallback -->

| Current version | Editable Markdown |
| --- | --- |
| Illustrative BNP lower-house seat-share model. | Illustrative BNP lower-house seat-share model. |

### `BES.figure.allocation.state.proposal.summary`

<!-- locator: index.html :: states.proposal.summary and HTML fallback -->

| Current version | Editable Markdown |
| --- | --- |
| BNP 72 · Jamaat 23 · all other parties 5 | BNP 72 · Jamaat 23 · all other parties 5 |

### `BES.figure.allocation.state.proposal.map-note`

<!-- locator: index.html :: states.proposal.mapNote and HTML fallback -->

| Current version | Editable Markdown |
| --- | --- |
| The supplied files do not contain party wins by division for this seat-share model. | The supplied files do not contain party wins by division for this seat-share model. |

### `BES.figure.allocation.state.proposal.a11y-description`

<!-- locator: index.html :: states.proposal.description -->

| Current version | Editable Markdown |
| --- | --- |
| Illustrative BNP seat-share proposal: BNP 72 seats, Jamaat 23, NCP 2, BKM 1 and other parties 2. | Illustrative BNP seat-share proposal: BNP 72 seats, Jamaat 23, NCP 2, BKM 1 and other parties 2. |

### `BES.figure.allocation.state.hare.deck`

<!-- locator: index.html :: states.hare.deck -->

| Current version | Editable Markdown |
| --- | --- |
| Party votes · Hare quota · seats allocated within eight divisions. | Party votes · Hare quota · seats allocated within eight divisions. |

### `BES.figure.allocation.state.hare.summary`

<!-- locator: index.html :: states.hare.summary -->

| Current version | Editable Markdown |
| --- | --- |
| BNP 54 · Jamaat 35 · seven parties represented | BNP 54 · Jamaat 35 · seven parties represented |

### `BES.figure.allocation.state.hare.map-note`

<!-- locator: index.html :: states.hare.mapNote -->

| Current version | Editable Markdown |
| --- | --- |
| No party majority in Barishal or Rangpur; Jamaat majority in Khulna. | No party majority in Barishal or Rangpur; Jamaat majority in Khulna. |

### `BES.figure.allocation.state.hare.a11y-description`

<!-- locator: index.html :: states.hare.description -->

| Current version | Editable Markdown |
| --- | --- |
| Hare quota: BNP 54 seats, Jamaat 35, NCP 4, IAB 3, BKM 2, Islamic Front 1 and Khelafat Majlis 1. | Hare quota: BNP 54 seats, Jamaat 35, NCP 4, IAB 3, BKM 2, Islamic Front 1 and Khelafat Majlis 1. |

### `BES.figure.allocation.state.dhondt.deck`

<!-- locator: index.html :: states.dhondt.deck -->

| Current version | Editable Markdown |
| --- | --- |
| The same party votes and divisions · D’Hondt allocation. | The same party votes and divisions · D’Hondt allocation. |

### `BES.figure.allocation.state.dhondt.summary`

<!-- locator: index.html :: states.dhondt.summary -->

| Current version | Editable Markdown |
| --- | --- |
| BNP 61 · Jamaat 36 · five parties represented | BNP 61 · Jamaat 36 · five parties represented |

### `BES.figure.allocation.state.dhondt.map-note`

<!-- locator: index.html :: states.dhondt.mapNote -->

| Current version | Editable Markdown |
| --- | --- |
| BNP majority in seven divisions; Jamaat majority in Khulna. | BNP majority in seven divisions; Jamaat majority in Khulna. |

### `BES.figure.allocation.state.dhondt.a11y-description`

<!-- locator: index.html :: states.dhondt.description -->

| Current version | Editable Markdown |
| --- | --- |
| D’Hondt: BNP 61 seats, Jamaat 36, NCP 1, IAB 1 and BKM 1. | D’Hondt: BNP 61 seats, Jamaat 36, NCP 1, IAB 1 and BKM 1. |

### `BES.figure.allocation.state.threshold.deck`

<!-- locator: index.html :: states.threshold.deck -->

| Current version | Editable Markdown |
| --- | --- |
| D’Hondt result with the two constitutional decision points. | D’Hondt result with the two constitutional decision points. |

### `BES.figure.allocation.state.threshold.summary`

<!-- locator: index.html :: states.threshold.summary -->

| Current version | Editable Markdown |
| --- | --- |
| BNP clears 51 alone · no party reaches 67 | BNP clears 51 alone · no party reaches 67 |

### `BES.figure.allocation.state.threshold.map-note`

<!-- locator: index.html :: states.threshold.mapNote -->

| Current version | Editable Markdown |
| --- | --- |
| The map is unchanged; the reference lines now show what the chamber can decide. | The map is unchanged; the reference lines now show what the chamber can decide. |

### `BES.figure.allocation.state.threshold.a11y-description`

<!-- locator: index.html :: states.threshold.description -->

| Current version | Editable Markdown |
| --- | --- |
| Under D’Hondt, BNP has 61 seats: above a 51-vote majority and below a two-thirds threshold of 67. | Under D’Hondt, BNP has 61 seats: above a 51-vote majority and below a two-thirds threshold of 67. |

### `BES.figure.allocation.axis.simple-majority`

<!-- locator: index.html :: drawBar() first reference label -->

| Current version | Editable Markdown |
| --- | --- |
| 51 · simple majority | 51 · simple majority |

### `BES.figure.allocation.axis.two-thirds`

<!-- locator: index.html :: drawBar() second reference label -->

| Current version | Editable Markdown |
| --- | --- |
| 67 · two-thirds | 67 · two-thirds |

### `BES.figure.allocation.axis.title`

<!-- locator: index.html :: drawBar() axis title -->

| Current version | Editable Markdown |
| --- | --- |
| Seats in a 100-seat chamber | Seats in a 100-seat chamber |

### `BES.figure.allocation.map.a11y.proposal-title`

<!-- locator: index.html :: updateMap() proposal title -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh divisions; no division allocation modelled | Bangladesh divisions; no division allocation modelled |

### `BES.figure.allocation.map.a11y.hare-title`

<!-- locator: index.html :: updateMap() Hare title -->

| Current version | Editable Markdown |
| --- | --- |
| Division majorities under Hare quota | Division majorities under Hare quota |

### `BES.figure.allocation.map.a11y.dhondt-title`

<!-- locator: index.html :: updateMap() D’Hondt title -->

| Current version | Editable Markdown |
| --- | --- |
| Division majorities under D’Hondt | Division majorities under D’Hondt |

### `BES.figure.allocation.map.a11y.proposal-division`

<!-- locator: index.html :: updateMap() proposal division template -->

| Current version | Editable Markdown |
| --- | --- |
| Dhaka: division composition is not available for the illustrative seat-share model. | {division}: division composition is not available for the illustrative seat-share model. |

### `BES.figure.allocation.map.a11y.division`

<!-- locator: index.html :: updateMap() modeled division template -->

| Current version | Editable Markdown |
| --- | --- |
| Dhaka: BNP majority; BNP 15, Jamaat 8, NCP 1. | {division}: {majority_status}; {seat_composition}. |

### `BES.figure.allocation.ui.seat-error`

<!-- locator: index.html :: allocation job error -->

| Current version | Editable Markdown |
| --- | --- |
| Seat comparison could not load. | Seat comparison could not load. |

### `BES.figure.allocation.ui.map-error`

<!-- locator: index.html :: allocation job error -->

| Current version | Editable Markdown |
| --- | --- |
| Division map could not load. | Division map could not load. |

### `BES.figure.allocation.ui.map-fallback`

<!-- locator: index.html :: initAllocationScrolly() map fallback -->

| Current version | Editable Markdown |
| --- | --- |
| The seat comparison remains available; the boundary file could not load. | The seat comparison remains available; the boundary file could not load. |

## Methodology

### `BES.methodology.heading`

<!-- locator: index.html :: [data-copy-id="BES.methodology.heading"] -->

| Current version | Editable Markdown |
| --- | --- |
| Methodology | Methodology |

### `BES.methodology.upper-house.summary`

<!-- locator: index.html :: [data-copy-id="BES.methodology.upper-house.summary"] -->

| Current version | Editable Markdown |
| --- | --- |
| Upper-house simulation | Upper-house simulation |

### `BES.methodology.upper-house.counterfactual`

<!-- locator: index.html :: [data-copy-id="BES.methodology.upper-house.counterfactual"] -->

| Current version | Editable Markdown |
| --- | --- |
| This is a mechanical counterfactual, not a forecast. It reuses lower-house constituency votes as though they were upper-house list preferences; a separate ballot could produce different choices. Excluding independent candidates is a design decision in this model, not a requirement of every proportional system. | This is a mechanical counterfactual, not a forecast. It reuses lower-house constituency votes as though they were upper-house list preferences; a separate ballot could produce different choices. Excluding independent candidates is a design decision in this model, not a requirement of every proportional system. |

### `BES.methodology.upper-house.formulas`

<!-- locator: index.html :: [data-copy-id="BES.methodology.upper-house.formulas"] -->

| Current version | Editable Markdown |
| --- | --- |
| The scrolly shows Hare and D’Hondt, the least and most disproportional of the four valid retained outcomes by the Gallagher index. Droop quota, Hagenbach-Bischoff quota and Webster/Sainte-Laguë are identical in every division-party cell in this dataset. The Imperiali quota and modified Imperiali quota outputs are excluded because the supplied implementation over-allocates the chamber to 101 and 105 seats. | The scrolly shows Hare and D’Hondt, the least and most disproportional of the four valid retained outcomes by the Gallagher index. Droop quota, Hagenbach-Bischoff quota and Webster/Sainte-Laguë are identical in every division-party cell in this dataset. The Imperiali quota and modified Imperiali quota outputs are excluded because the supplied implementation over-allocates the chamber to 101 and 105 seats. |

### `BES.methodology.upper-house.allocation`

<!-- locator: index.html :: [data-copy-id="BES.methodology.upper-house.allocation"] -->

| Current version | Editable Markdown |
| --- | --- |
| Division magnitudes are apportioned from registered voters with the Hare largest-remainder method. Party seats are then allocated within each division with no party-vote eligibility threshold, levelling tier, candidate-list rule or specified tie-break. The source file should be checked against the authoritative election record before publication. | Division magnitudes are apportioned from registered voters with the Hare largest-remainder method. Party seats are then allocated within each division with no party-vote eligibility threshold, levelling tier, candidate-list rule or specified tie-break. The source file should be checked against the authoritative election record before publication. |

### `BES.methodology.country-comparison.summary`

<!-- locator: index.html :: [data-copy-id="BES.methodology.country-comparison.summary"] -->

| Current version | Editable Markdown |
| --- | --- |
| Opening country comparison | Opening country comparison |

### `BES.methodology.country-comparison.taxonomy`

<!-- locator: index.html :: [data-copy-id="BES.methodology.country-comparison.taxonomy"] -->

| Current version | Editable Markdown |
| --- | --- |
| Electoral system classifications follow the International IDEA taxonomy. A country is counted as having *proportional seats* if its lower house uses List PR, MMP, a parallel system or STV; a *separate national mandate* if its head of state is directly elected by any method; and a *second chamber* if its legislature has an upper house. Second chambers vary widely: some represent territories, while others primarily scrutinise and revise legislation. | Electoral system classifications follow the International IDEA taxonomy. A country is counted as having *proportional seats* if its lower house uses List PR, MMP, a parallel system or STV; a *separate national mandate* if its head of state is directly elected by any method; and a *second chamber* if its legislature has an upper house. Second chambers vary widely: some represent territories, while others primarily scrutinise and revise legislation. |

### `BES.methodology.country-comparison.sources`

<!-- locator: index.html :: [data-copy-id="BES.methodology.country-comparison.sources"] -->

| Current version | Editable Markdown |
| --- | --- |
| The country examples use official institutional sources: Peru’s [2026 electoral plan](https://www.onpe.gob.pe/modMarco-Legal/POE-EG-2026-V03.pdf) and [bicameral guide](https://eg2026.onpe.gob.pe/bicameralidad/), the [Electoral Commission of Ghana](https://ec.gov.gh/electoral-system/), and the [Parliament of Australia](https://www.aph.gov.au/About_Parliament/Senate/About_the_Senate). | The country examples use official institutional sources: Peru’s [2026 electoral plan](https://www.onpe.gob.pe/modMarco-Legal/POE-EG-2026-V03.pdf) and [bicameral guide](https://eg2026.onpe.gob.pe/bicameralidad/), the [Electoral Commission of Ghana](https://ec.gov.gh/electoral-system/), and the [Parliament of Australia](https://www.aph.gov.au/About_Parliament/Senate/About_the_Senate). |

### `BES.methodology.country-comparison.limitations`

<!-- locator: index.html :: [data-copy-id="BES.methodology.country-comparison.limitations"] -->

| Current version | Editable Markdown |
| --- | --- |
| Population and Freedom House ratings in the underlying file date from 2009 and should be refreshed before publication. The outlier finding is specific to this 47-country comparison, not every country in the world: Papua New Guinea and several microstates fall below the population threshold and also lack all three arrangements. | Population and Freedom House ratings in the underlying file date from 2009 and should be refreshed before publication. The outlier finding is specific to this 47-country comparison, not every country in the world: Papua New Guinea and several microstates fall below the population threshold and also lack all three arrangements. |

### `BES.methodology.country-comparison.reserved-seats`

<!-- locator: index.html :: [data-copy-id="BES.methodology.country-comparison.reserved-seats"] -->

| Current version | Editable Markdown |
| --- | --- |
| Bangladesh’s lower house is not purely first-past-the-post. Fifty seats are reserved for women and allocated in proportion to party strength — a partial corrective inside the chamber, but one that cannot alter which party controls it. | Bangladesh’s lower house is not purely first-past-the-post. Fifty seats are reserved for women and allocated in proportion to party strength — a partial corrective inside the chamber, but one that cannot alter which party controls it. |

## Party display labels

### `BES.label.party.bnp`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| BNP | BNP |

### `BES.label.party.jamaat`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| Jamaat | Jamaat |

### `BES.label.party.ncp`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| NCP | NCP |

### `BES.label.party.iab`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| IAB | IAB |

### `BES.label.party.bkm`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| BKM | BKM |

### `BES.label.party.islamic-front`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| Islamic Front | Islamic Front |

### `BES.label.party.khelafat-majlis`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| Khelafat Majlis | Khelafat Majlis |

### `BES.label.party.independent`

<!-- locator: index.html :: party display label -->

| Current version | Editable Markdown |
| --- | --- |
| Independent candidates | Independent candidates |

### `BES.label.party.other`

<!-- locator: index.html :: partyOrder/party legend display -->

| Current version | Editable Markdown |
| --- | --- |
| Other parties | Other parties |
