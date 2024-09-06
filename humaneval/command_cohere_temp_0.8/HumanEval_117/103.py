```python
def count_cons(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    res = []
    for word in words:
        cnt = count_cons(word)
        if cnt == n:
            res.append(word)
    return res
```

The provided Python script defines a function `select_words(s, n)` that takes a string `s` and an integer `n` as input, returning a list of all words from the string `s` that contain exactly `n` consonants. To achieve this, the function counts the number of consonants in each word using the `count_cons` helper function and adds them to the result list if they contain exactly `n` consonants.