```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or all(c not in letters for c in s) else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a single argument, `s`, representing a string. This function performs different operations based on the characters present in the string. If the string is empty or contains no letters from the Latin alphabet, it simply swaps the case of all characters and returns the resulting string. Otherwise, it iterates through each character in the string and individually swaps its case if it's a letter, while leaving non-letter characters unchanged. The resulted string is then returned.