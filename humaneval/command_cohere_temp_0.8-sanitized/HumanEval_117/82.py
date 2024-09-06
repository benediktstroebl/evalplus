def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    """
    consonant_count = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonant_count += 1
    return consonant_count
def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    """
    words = s.split()
    selected_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            selected_words.append(word)

    return selected_words if selected_words else ["None"]
n = 3