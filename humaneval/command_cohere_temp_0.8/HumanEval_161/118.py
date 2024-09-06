```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz']
```
The function takes a string and checks if it contains any letters. If it does not, it simply swaps the string case. Otherwise, it swaps the case of each letter, leaving non-letter characters unchanged. This behavior is achieved using the `swapcase()` method and filtering out letters from the string. The resulting string is then returned.