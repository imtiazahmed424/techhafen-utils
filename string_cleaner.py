def clean_text(text: str) -> str:
    """Removes extra spaces and symbols from text."""
    return " ".join(text.split())
