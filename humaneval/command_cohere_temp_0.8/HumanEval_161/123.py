```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s` which performs the needed operations as directed in the problem statement. The `swapcase` function is used for reversing the case of alphabetic characters, and for non-alphabetic characters, the function just keeps them as they are. The `join` function is then used to concatenate the modified characters to form the required result.