import json

def prettify_json(data: str) -> str:
    """Formats JSON for readability."""
    try:
        parsed = json.loads(data)
        return json.dumps(parsed, indent=4)
    except json.JSONDecodeError:
        return "Invalid JSON input."
