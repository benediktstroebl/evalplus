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
    Returns a list of words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    if len(s) == 0:
        return []
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is a helper function that calculates the number of consonants in any given word. This function is essential in achieving the primary task of identifying words with a specific number of consonants. 

The `select_words` function acts as the main driver behind the solution. Firstly, it splits the input string into an array of space-separated words. Then, it iterates through each word while relying on the `count_consonants` function to tally the number of consonants. If a word possesses the exact number of consonants as requested, it gets added to the result array. Finally, the function returns this array of qualifying words. 

The approach demonstrates a clear separation of concerns and adheres firmly to the principle of simplicity. It also achieves the desired functionality efficiently and flexibly, capable of handling any string and integer input.