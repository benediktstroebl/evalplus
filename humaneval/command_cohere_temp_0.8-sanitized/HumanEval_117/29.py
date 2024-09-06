def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (case-insensitive).
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_lowercase = 'aeiouAEIOU'
    vowel_uppercase = 'AEIOU'
    return sum(1 for char in word if char.lower() not in vowel_lowercase and char not in vowel_uppercase)
def select_words(s, n):
    """
    Given a string s and an integer n, return a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    A word contains a vowel if it contains at least one vowel character, and contains a consonant if it contains at least one consonant character.
    If the string s is empty then the function should return an empty list.
    """
    if not s:
        return []

    words = s.split(' ')
    result = []

    for word in words:
        word_consonants = count_consonants(word)
        if word_consonants == n:
            result.append(word)

    return result