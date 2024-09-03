def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels
    Returns: string without vowels
    """
    return ''.join(c for c in text if c.isalpha(97, 59, 65, 123, 91))