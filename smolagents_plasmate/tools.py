"""Plasmate tool for HuggingFace Smolagents."""

import subprocess
from smolagents import Tool


class PlasmateFetchTool(Tool):
    name = "plasmate_fetch"
    description = (
        "Fetch a web page and get clean semantic content using Plasmate. "
        "Returns structured SOM (Semantic Object Model) with 10-16x fewer "
        "tokens than raw HTML."
    )
    inputs = {"url": {"type": "string", "description": "The URL to fetch"}}
    output_type = "string"

    def forward(self, url: str) -> str:
        try:
            result = subprocess.run(
                ["plasmate", "fetch", url],
                capture_output=True,
                text=True,
                timeout=30,
            )
            return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
        except FileNotFoundError:
            return "Plasmate not installed. Run: pip install plasmate"
        except subprocess.TimeoutExpired:
            return f"Timeout fetching {url}"
