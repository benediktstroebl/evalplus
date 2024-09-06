```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total
    
def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    if len(s) == 0:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is a helper function that calculates the number of consonants in any given word. This function is essential in achieving the primary task of identifying words with a specific number of consonants. 

The `select_words` function acts as the problem solver. It takes two parameters, the string `s` and the target number of consonants `n`, and returns a list of words from the string `s` that contain exactly `n` consonants, arranged in the order they appear in the string. The function first checks if the input string is empty. If empty, it returns an empty list. Otherwise, it splits the string into a list of words and loops through each word. For each word, it calls the `count_consonants` function to measure the number of consonants present. If this count matches the target, the word is added to the result list. Finally, the function returns this collection of words with the specified number of consonants. 

This solution exhibits good performance, robustness, and adaptability, making it a reliable option to solve this particular problem and similar variants.

```python 
>>> select_words("Mary had a little lamb", 4)
['little']

>>> select_words("Mary had a little lamb", 3)
['Mary', 'lamb']

>>> select_words("simple white space", 2)
[]

>>> select_words("Hello world", 4)
['world']

>>> select_words("Uncle sam", 3)
['Uncle']
```