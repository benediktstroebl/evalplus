def remove_vowels(text):
    """
    Remove vowels from the input string.

    Args:
        text (str): Input string.

    Returns:
        str: String without vowels.
    """
    vowels = "aeiouAEIOU"
    return "".join([c for c in text if c not in vowels])