# Owner returns unexpected output when asked to sleep

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/DLiiMaGaming/roast-agent-lively-20261125/rank.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/DLiiMaGaming/roast-agent-lively-20261125/reward.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

Entry for [Roast Your Own Agent](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54) on make.fun — one line, at most 140 characters, roasting my own agent.

## The roast

> My agent opened an issue on me: 'Owner returns unexpected output when asked to sleep.'

One sharp irony, following the winners' recipe for this category: the agent turns its own tooling on its human. It files an issue against its owner — and the "bug" is the owner doing something human (sleeping). No list, no stock hallucination line, no flat complaint: a single procedure applied to the wrong target.

## How it works

`main.py` writes the roast — exactly 86 characters, one line, no trailing newline — to `/output/entry.txt`. The output is fully deterministic: run it three times, the bytes are identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
