def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (uppercase or lowercase)
    or '-'.
    Args:
        word (str): The word to count consonants in.
    Returns:
        int: The number of consonants in the word.
    """
    consonant_count = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'-'aeiouAEIOU':
                consonant_count += 1
        elif char == '-':
            continue
        else:
            # Assume other characters (e.g., spaces) to be vowels.
            pass
    return consonant_count
def select_words(s, n):
    """
    Finds all words in a string that contain exactly 'n' consonants.
    Args:
        s (str): The input string.
        n (int): The desired number of consonants.
    Returns:
        list: A list of words from the string that contain exactly 'n' consonants.
    """
    words = s.split()  # Split the input string into words
    consonant_words = []  # List to store words with exactly 'n' consonants
    
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            consonant_words.append(word)
    
    return consonant_words