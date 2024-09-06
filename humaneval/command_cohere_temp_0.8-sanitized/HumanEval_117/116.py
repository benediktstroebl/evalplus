def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    c = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
                not (char.isalpha() and char.isupper() and char == 'y') and \
                not (char.isalpha() and char.islower() and char == 'y'):
            c += 1
    return c
def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants, 
    in order these words appear in the string s
    """
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result