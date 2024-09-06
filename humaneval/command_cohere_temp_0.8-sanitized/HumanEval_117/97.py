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
    Given a string s and an integer n, this function returns a list of all words 
    from string s that contain exactly n consonants, in order these words appear 
    in the string s. If the string s is empty then the function should return an 
    empty list.
    """
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result