def fix_spaces(text):
    """
    Replaces all spaces with underscores, and doubles consecutive spaces with - .

    Args:
        text (str): Input string

    Returns:
        str: Fixed string with spaces replaced with underscores and - .
    """
    fixed = text.replace(" ", "_")
    if fixed != text:
        raise ValueError("Failed to fix spaces.")
    return fixed