```python
def count_consonants(word):
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct

def select_words(s, n):
    words = s.split()
    res = []
    for w in words:
        if count_consonants(w) == n:
            res.append(w)
    return res if res else ['']
```

The function `count_consonants(word)` calculates the number of consonants in a given word, considering both lowercase and uppercase letters as in the given examples. The main function `select_words(s, n)` splits the input string into a list of words, and then it iterates through the words to collect those that have exactly the desired number of consonants. The function returns an empty list if the input string is empty, and it handles cases where the number of consonants requested is larger than the total number of consonants in the input string.