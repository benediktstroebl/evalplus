```python
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
    Returns a list of all words from string s that contain exactly n consonants, 
    in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    # Ensure the input string is not empty and the number of consonants to find is a natural number.
    if not s or not isinstance(n, int) or n < 0:
        return []

    words = s.split()
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)

    return result
```

The `count_consonants` function is a helper used to determine the total consonants in a given word, which is essential for solving this problem. It iterates over each character in the word, checking if each character is a consonant. The `select_words` function is the main function to solve the problem, it splits the input string into a list of words, then checks each word's consonant count, and adds the suitable words to the result list. Lastly, the function returns the list of words with exactly n consonants. 

This solution has a time complexity of O(n + m), where n is the number of words and m is the maximum word length in the input string. The space complexity is O(1) since the function only operates on a single input string and a list to store the result words. 

This approach assumes that the input string only contains letters and spaces, but it handles cases where the input parameters are empty or where n is less than 0, ensuring robustness against unexpected inputs.