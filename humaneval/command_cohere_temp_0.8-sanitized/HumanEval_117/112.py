def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                (char != 'y' or word[0] in 'aeiou') and char != 'w' and char != 'h':
            total += 1
    return total
def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result