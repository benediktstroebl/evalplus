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
The `count_consonants` function counts the number of consonants in a given word, including when the letter appears twice or more in the word. This function helps the main `select_words` function to get the desired results.

The `select_words` function splits the input string into a list of words, and then checks each word's consonant count, pushing it to a result list if it matches the desired `n` or ignoring it otherwise. The function returns an empty list if the input string is empty.

Both functions are self-contained and independent as they don't depend on any external libraries and are inherently connected as they are designed to solve the mentioned problem together. Hence, they can be easily copied and pasted into a project to get immediate results without any dependency or additional work.