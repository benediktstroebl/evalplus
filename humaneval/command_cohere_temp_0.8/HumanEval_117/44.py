```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'y' and char != 'h':
            total += 1
    return total

def select_words(s, n):
    """Return list of words containing exactly n consonants"""
    words = []
    for word in s.split():
        consonant_count = count_consonants(word)
        if consonant_count == n:
            words.append(word)
    return words
```
The `count_consonants` function is used to count the number of consonants in a given word. The `select_words` function splits the input string into words, counts the number of consonants in each word using the previous function, and adds the word to the result list if the count is equal to the specified number of consonants `n`. 

This solution has a time complexity of O(n + m) where n is the number of words and m is the maximum word length. The space complexity is O(n) as well, due to the storage of intermediate words. 

The presumed assumptions are that the input string contains only letters and spaces, and that the given natural number n is not greater than the number of consonants in any word of the given string.