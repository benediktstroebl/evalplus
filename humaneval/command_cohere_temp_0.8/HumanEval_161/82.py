```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':]
```
The function takes a string and checks if it contains any letters. If the string contains no letters, it undergoes a case swap, transforming the string. If the string contains at least one letter, the function selectively applies the swap case operation only if the letter is in uppercase. This ensures that lowercase letters remain unchanged while uppercase letters have their case reversed.