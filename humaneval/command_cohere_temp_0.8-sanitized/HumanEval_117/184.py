def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    Args:
        word (str): The word to count consonants in.
    Returns:
        int: The number of consonants in the word.
    """
    consonant_count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
                char.isalpha():
            if char.lower() != char.upper():
                consonant_count += 1
            else:
                consonant_count += 2
    return consonant_count
def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    Args:
        s (str): The input string.
        n (int): The number of consonants to filter on.
    Returns:
        list: A list of words containing exactly n consonants.
    """
    words = s.split()  # Split the string into words
    selected_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            selected_words.append(word)

    return selected_words if selected_words else []