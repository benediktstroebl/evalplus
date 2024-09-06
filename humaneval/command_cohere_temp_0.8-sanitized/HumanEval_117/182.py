def count_consonants(word):
    """
    Counts the number of consonants in a word.
    A consonant is a letter that is not a vowel (case-insensitive)
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return len([c for c in word.lower() if c not in vowels and c != ' '])
def select_words(s, n):
    """
    Given a string s and an integer n, returns a list of all words from s that contain exactly n consonants.
    """
    words = s.split(' ')
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result