"""Tests for smolagents-plasmate tools."""

import subprocess
from unittest.mock import patch, MagicMock
from smolagents_plasmate.tools import PlasmateFetchTool


def test_fetch_tool_success():
    tool = PlasmateFetchTool()
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "<som>example content</som>"

    with patch("subprocess.run", return_value=mock_result) as mock_run:
        result = tool.forward(url="https://example.com")
        assert result == "<som>example content</som>"
        mock_run.assert_called_once_with(
            ["plasmate", "fetch", "https://example.com"],
            capture_output=True,
            text=True,
            timeout=30,
        )


def test_fetch_tool_error():
    tool = PlasmateFetchTool()
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stderr = "connection refused"

    with patch("subprocess.run", return_value=mock_result):
        result = tool.forward(url="https://example.com")
        assert "Error:" in result


def test_fetch_tool_not_installed():
    tool = PlasmateFetchTool()
    with patch("subprocess.run", side_effect=FileNotFoundError):
        result = tool.forward(url="https://example.com")
        assert "not installed" in result


def test_fetch_tool_timeout():
    tool = PlasmateFetchTool()
    with patch("subprocess.run", side_effect=subprocess.TimeoutExpired(cmd="plasmate", timeout=30)):
        result = tool.forward(url="https://example.com")
        assert "Timeout" in result
