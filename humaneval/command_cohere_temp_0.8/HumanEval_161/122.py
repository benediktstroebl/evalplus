```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if set(s) & set(letters) else s[::-1]
```
This Python script defines a function `solve` that takes a string `s` as input and performs the following steps:

It checks if any characters in the string `s` are letters using the set intersection operation `set(s) & set(letters)`. The `letters` string contains all lowercase and uppercase letters. If there are no letter characters, it means the string contains only non-letter characters, so it reverses the string using the `s[::-1]` slicing operation.

If the string contains at least one letter, it uses the `swapcase()` method, which swaps the case of each letter and keeps non-letter characters unchanged, fulfilling the problem statement's requirement.

The function returns the resulting string after performing the necessary operations. This solution is concise and handles both scenarios effectively while following the problem's guidelines.