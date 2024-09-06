```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) == set() else s.swapcase()[letters == 'abcdefghijklmnopqrstuvwxyz':]
```
The function takes a string and checks if it contains any letters. If the string contains no letters, it swaps the strings case. If the string contains at least one letter, it swaps the case of the letters only. This is achieved by using the built-in `swapcase()` method and filtering the string with a boolean condition. The filtering condition checks if the character is in the string `abcdefghijklmnopqrstuvwxyz`, meaning that it should swap only the lower case letters.