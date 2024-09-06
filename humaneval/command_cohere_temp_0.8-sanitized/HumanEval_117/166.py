def select_words(s, n):
    """
    Find words in a string that contain exactly 'n' consonants.
    
    Args:
    - s (str): Input string.
    - n (int): Number of consonants required in each word.

    Returns:
    - list: List of words containing exactly 'n' consonants.
    """
    # Ensure the input string is not empty
    if not s:
        return []

    # Split the string into individual words
    words = s.split()

    # Filter words based on the condition
    selected_words = [word for word in words if len(set(word.replace(' ', ''))) == n]

    return selected_words