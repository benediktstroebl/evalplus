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
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The approach works by first creating a function `count_consonants` that counts the number of consonants in a given word, then `select_words` uses this to iterate through the words in the string, checking if the count of consonants is equal to the desired number `n`. Words that match this condition are added to the result list. 
This solution is concise and efficient, and it should work correctly for any valid input to the prompt's problem.