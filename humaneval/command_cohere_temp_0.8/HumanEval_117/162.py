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
        cnt = count_consonants(word)
        if cnt == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into a list of words, iterates through each word, and compares its consonant count to the desired `n`, adding it to the `result` list if they match.

You can test this function with various cases to ensure it aligns with the problem's specifications.