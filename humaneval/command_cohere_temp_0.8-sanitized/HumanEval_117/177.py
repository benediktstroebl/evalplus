def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (same as python's 'ascii_lowercase').
    """
    vowels = "aeiou"
    count = 0
    for char in word:
        if char not in vowels:
            count += 1
    return count
def select_words(s, n):
    """
    This function takes a string s and an integer n, and returns a list of all words from string s
    that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    words = s.split(' ')    # Split the input string into a list of words, accounting for spaces
    result = []              # List to hold the final result
    
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    
    return result