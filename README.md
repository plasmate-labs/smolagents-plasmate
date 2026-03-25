# smolagents-plasmate

Plasmate web browsing tool for HuggingFace Smolagents. Get clean semantic page content using 10-16x fewer tokens than Chrome.

## Install

```bash
pip install smolagents-plasmate
```

## Usage

```python
from smolagents import CodeAgent, HfApiModel
from smolagents_plasmate import PlasmateFetchTool

agent = CodeAgent(tools=[PlasmateFetchTool()], model=HfApiModel())
agent.run("Fetch https://example.com and summarize the content")
```

## What is Plasmate?

[Plasmate](https://plasmate.dev) is a lightweight web browsing engine for AI agents. It returns a Semantic Object Model (SOM) instead of raw HTML, reducing token usage by 10-16x compared to headless Chrome.

## Links

- [Plasmate Documentation](https://plasmate.dev)
- [W3C Web Agents Community Group](https://www.w3.org/community/web-agents/)
- [GitHub](https://github.com/nicobailey/plasmate)

## License

Apache 2.0
