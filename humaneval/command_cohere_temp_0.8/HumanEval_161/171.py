```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or all(c not in letters for c in s) else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a single argument `s`, which is the input string. 

The function first checks if the string is empty or if it contains any letters. The `letters` variable is a string containing all lowercase and uppercase letters, used for this check. If the string either empty or doesn’t contain any letters, it uses the `swapcase` method to swap the characters' cases and return the resulting string. If the string contains at least one letter, the function goes through each character in the string and swaps its case if it's a letter. Otherwise, it leaves the character as is and builds the new string this way. This is what the `join` method is used for.