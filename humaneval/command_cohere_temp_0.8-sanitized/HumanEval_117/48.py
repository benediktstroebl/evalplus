def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    consonants are letters that are not vowels (A, E, I, O, U)
    """
    count = 0
    for char in word:
        if char not in 'AEIOU':
            count += 1
    return count
def select_words(s, n):
    """
    Given a string s and an integer n, return a list of all words from string s
    that contain exactly n consonants, in order these words appear in the string s.
    A word contains exactly n consonants if the number of consonants in that word is equals to n.
    """
    words = [w for w in s.split(' ') if w]
    return [word for word in words if count_consonants(word) == n]