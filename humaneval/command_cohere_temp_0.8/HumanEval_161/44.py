```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s`, where based on the given string's characters, it either swaps the case of letters or keeps them as they are. To achieve this, it uses a list comprehension combined with the `swapcase()` method for alphabetic characters and the `join()` method to concatenate the modified characters into a single string.