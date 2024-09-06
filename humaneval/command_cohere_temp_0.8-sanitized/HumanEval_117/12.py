def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    Args:
        word (str): The word to count consonants in.
    Returns:
        int: The number of consonants in the word.
    """
    count = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            count += 1
    return count
def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    Args:
        s (str): The input string.
        n (int): The number of consonants to filter by.
    Returns:
        list: A list of words from the string s that contain exactly n consonants.
    """
    words = s.split()  # Split the string into words
    filtered_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            filtered_words.append(word)

    return filtered_words