```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            count += 1
    return count

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into a list of words, iterates through each word, and checks if its consonant count matches the required count `n`. If a word has exactly `n` consonants, it's added to the `result` list, and finally, the function returns this list. 

This solution adheres to the problem statement by considering only letters (not including spaces) when counting consonants and correctly identifies the appearance order of the selected words in the input string.