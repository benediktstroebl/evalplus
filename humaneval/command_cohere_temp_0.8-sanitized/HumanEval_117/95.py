def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (case-insensitive).
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return len([c for c in word.lower() if c not in vowels and c != ' '])
def select_words(s, n):
    """
    Given a string s and an integer n, return a list of all words from string s that contain exactly n consonants.
    If the string s is empty or the number n is larger than the number of consonants in s, return an empty list.
    """
    words = s.split(' ')
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)

    return result