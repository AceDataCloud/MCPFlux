"""Utility functions for MCP Flux server."""

import json
from typing import Any


def format_image_result(data: dict[str, Any]) -> str:
    """Format image generation result as JSON.

    Args:
        data: API response dictionary

    Returns:
        JSON string representation of the result
    """
    return json.dumps(data, ensure_ascii=False, indent=2)


def format_task_result(data: dict[str, Any]) -> str:
    """Format task query result as JSON.

    Args:
        data: API response dictionary

    Returns:
        JSON string representation of the result
    """
    return json.dumps(data, ensure_ascii=False, indent=2)
