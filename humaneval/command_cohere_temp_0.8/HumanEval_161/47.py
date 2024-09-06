```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[0::2 if c.isalpha() else 1 for c in s]
```
The function uses `swapcase()` to reverse the case of non-letter characters and alternates between upper and lower case for letter characters. As claimed in the prompt, for a pure numeric or other non-letter string, the whole string gets reversed. And for a string containing letters, alternates between upper and lower case.