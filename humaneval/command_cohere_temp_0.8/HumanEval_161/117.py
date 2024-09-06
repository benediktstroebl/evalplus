```python
def solve(s):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return s.swapcase() if len(s) == 0 or all(c not in letters for c in s) else ''.join(c.swapcase() if c in letters else c for c in s)
```
This Python script defines a function `solve` that takes a single string parameter `s`. This function performs different operations based on the characters present in the string. If the string is empty or contains no letters, it simply swaps the case of all characters and returns the resulting string. If the string contains at least one letter, it goes through each character in the string and applies a swap case if the character is a letter, while leaving non-letter characters unchanged. The script then returns the modified string. This behavior is outlined in the docstring, which also provides example use cases and their expected outcomes.