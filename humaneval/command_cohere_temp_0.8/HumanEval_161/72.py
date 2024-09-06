```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or all(c not in letters for c in s) else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a single string parameter `s`. The function inspects each character in the string, using an internal letter dictionary for efficiency. If the string is empty or contains only non-letter characters, it employs the `swapcase` method to reverse the entire string. Otherwise, for each letter character, it toggles its case while leaving non-letter characters unchanged. The final output is a string with the intended transformations applied, as specified in the problem description.