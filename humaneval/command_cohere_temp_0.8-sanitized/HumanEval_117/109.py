def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
def select_words(s, n):
    """
    Recursive implementation to extract words containing exactly n consonants.
    """
    # base case: if the string is empty or we reach the end of a word, return
    if not s or len(s) == 1:
        return []
    # if current word satisfies the condition, add it to the result
    if count_consonants(s[:len(s) - 1]) == n:
        result = select_words(s[len(s) - 1:], n) + [s[:len(s) - 1]]
        return result
    # otherwise, continue searching in the next word
    else:
        return select_words(s[1:], n)