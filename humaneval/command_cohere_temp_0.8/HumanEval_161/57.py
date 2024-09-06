```python
def solve(s):
    return ''.join(c.swapcase() if c.isalpha() else c for c in s)
```
This Python script defines a function `solve` taking one parameter `s` which performs the task as described in the prompt. It uses Python's `swapcase` function which reverses the case of alphabetic characters, and joins the characters back into a string without altering their non-alphabetic characters' cases.