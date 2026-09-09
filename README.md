<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright 2026 flxk1 -->
# loomground-brief

**What is the minimum a supervisor must read?**

Selects the minimum unresolved material required for human review.

## Install

```
pip install loomground-brief
```

## Usage

```python
from loomground_brief import oversight_brief
brief = oversight_brief(premises=premises, space=space, divergences=divergences)
brief.items, brief.settled_omitted
```

## Interface

- inputs (all optional): `premises: Iterable[StatusedPremise]` · `space: DecisionSpace` · `negative_space: dict` · `divergences: (ref, why)`
- output: `OversightBrief(items: BriefItem(kind, ref, why), settled_omitted: int)`, ordered by `KIND_ORDER`
- from solver: `decision.DecisionSpace` · `epistemic_status.StatusedPremise` · `epistemic_status.root_causes`

## Family

Diagnostic operator; consumes `loomground-solver` 0.5; consumed by hosts. Pipeline: `source → loomground-ingest → loomground-versum → loomground-solver → loomground-brief`. Operator contract: [spec/OPERATORS.md](https://github.com/flxk1/loomground/blob/main/spec/OPERATORS.md). [docs/operator.md](docs/operator.md).

## Status

0.1.0 · 16 tests · Python >=3.10 · solver 0.5

## License

Apache-2.0 `LICENSES/Apache-2.0.txt` (code) · CC-BY-4.0 `LICENSES/CC-BY-4.0.txt` (README) · `NOTICE`
