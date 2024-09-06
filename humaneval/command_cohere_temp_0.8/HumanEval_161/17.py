```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the given string's characters, it either swaps the case of letters or leaves non-letter characters unchanged, and subsequently returns the resulting string. The `join` function is utilized to concatenate the modified characters back into a single string.