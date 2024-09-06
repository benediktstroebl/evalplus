```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            total += 1
    return total
    
def select_words(s, n):
    """
    Given a string s and a natural number n, return a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `select_words` function uses the `count_consonants` helper function to calculate the total consonants in each word as it iterates through the split words from the input string. 

The split words are stored in the `words` variable, and the appropriate ones with a consonant count of `n` are added to the `result` list and returned. 

This solution assumes the input string contains only letters and spaces, which is the assumption stated in the problem.

Also, the code handles the case when `s` is an empty string by returning an empty list since there are no words in an empty string.

Note: the assumption that the input contains only letters and spaces can be easily violated in various ways, for example, with numbers, special characters, or diacritics on letters. This could be improved by updating the `count_consonants` function to handle different cases and extensively test against different types of characters.