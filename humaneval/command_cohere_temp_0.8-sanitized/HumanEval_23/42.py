def strlen(s: str) -> int:
    """Returns the length of a string, handles errors."""
    try:
        return len(s)
    except TypeError:
        raise TypeError("Input must be a string")