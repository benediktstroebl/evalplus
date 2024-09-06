```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string `s` as input and first initializes a counter `cnt` to 0. It then iterates through the string, checking if the index `i` is even and the character at that index is an uppercase vowel. If both conditions are met, it increments `cnt`. Finally, the function returns the resulting count, which represents the number of uppercase vowels in even indices of the given string.