```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                (char != 'y' or word[0] == 'y') and (char != 'h' or word[0] == 'h'):
            total += 1
    return total

def select_words(s, n):
    """Return list of words with exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is introduced first, which calculates the number of consonants in a given word. This is necessary to optimize the solution for the given problem.

Then, the `select_words` function is defined, which applies the `count_consonants` function to each word in the string and adds the word to the result list if it contains exactly `n` consonants.

Both functions are standalone and do not rely on external variables, thus solving the problem self-contained.

This approach achieves a time complexity of O(n + m) where n is the number of words and m is the maximum number of consonants in a word. The space complexity is O(1) since both functions do not store data externally.