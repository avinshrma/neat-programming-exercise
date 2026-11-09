# Case Summary

Objectives from [README.md](README.md), checked against `src/reportinput/report_params.py` and `tests/test_report_params.py`.

## Checkpoints

- [x] Find the common elements of the two inputs
- [x] Matching is case-insensitive
- [x] Result is a unique list of lowercase strings
- [x] No partial matches (e.g. "pineapple" vs "apple")
- [x] README example returns `["frog", "fish", "apple", "fox"]`
- [x] `pip install -e .` setup works (`reportinput` importable from `.venv`)
- [x] A number of meaningful unit tests (5 tests, all passing)

## Test coverage

| Test | Covers |
|---|---|
| `test_gen_params_matches_readme_example` | README example |
| `test_gen_params_trims_whitespace_and_removes_duplicates` | Whitespace trimming, de-duplication |
| `test_gen_param_simple_casing` | Case-insensitivity |
| `test_gen_params_matches_whole_tokens_only` | No partial matches |
| `test_gen_params_handles_empty_inputs_and_no_matches` | Empty inputs, no overlap |

## Notes

- Result order follows the first input; the README does not specify an order.
- `from typing import List` in `report_params.py` is unused.
