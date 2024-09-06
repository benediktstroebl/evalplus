```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the given string's characters, it either swaps the case of letters or keeps them as they are. In the latter case, this function returns the modified string.