```python
def count_consonants(word):
    cs = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cs += 1
    return cs

def select_words(s, n):
    words = []
    word = ""
    for c in s:
        if c == ' ':
            if count_consonants(word) == n:
                words.append(word)
            word = ""
        else:
            word += c
    if count_consonants(word) == n:
        words.append(word)
    return words
```
The provided Python script implements the `select_words` function, which takes a string `s` and an integer `n` as input. This function returns a list of all words from the string `s` that contain exactly `n` consonants. It achieves this by iterating through the string, tracking consonant counts in each word. Upon encountering a space, it checks if the current word has exactly `n` consonants; if so, it adds the word to the result list. After processing the entire string, any remaining words are checked for the target consonant count and added to the list. The script ensures correctness and flexibility in handling different input cases, providing an efficient solution to the problem.