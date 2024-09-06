```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
    
def select_words(s, n):
    """
    Selects words from a string that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is a helper function that calculates the number of consonants in any given word. 

The `select_words` takes a string that contains only letters and spaces as input, and splits it into a list of words. It then iterates through each word, calculating the number of consonants they contain with the help of the previous helper function. If the number of consonants matches the target number `n`, the word is added to the `result` list, which is returned after all words have been processed.

Both functions are designed to efficiently solve the problem and adhere to the assumption that the input string contains only letters and spaces. 

This approach provides a straightforward way to meet the problem requirements, as well as achieve best performance when handling large inputs.