```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cnt += 1
    return cnt

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

This solution focuses on simplicity and readability while achieving the problem's core requirement. Feel free to ask if you'd like to discuss any aspect of the code further!