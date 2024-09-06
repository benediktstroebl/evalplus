def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                (char != 'y' or word[1:] != 'ay' and word[1:] != 'ey' and word[1:] != 'iy' and word[1:] != 'oy' and word[1:] != 'uy'):
            if char != 'w' and char != 'h':
                total += 1
        elif char == 'y' and word[1:] == 'ay' or word[1:] == 'ey' or word[1:] == 'iy' or word[1:] == 'oy' or word[1:] == 'uy':
            total += 1
    return total
def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    words = s.split(' ')
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result