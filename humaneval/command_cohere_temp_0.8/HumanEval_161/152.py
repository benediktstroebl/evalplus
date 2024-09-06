```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]
```
The function takes a string and checks if it contains any letters. If it doesn't, it simply calls `swapcase()` to reverse the string. If it does contain letters, it uses a conditional to only reverse the letters, leaving non-letter characters unchanged. This strategy is given by the expression `s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]`.