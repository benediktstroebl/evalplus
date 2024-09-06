```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to the opposite case and leaves non-alphabetic characters unchanged. It joins the characters back together to form the resulting string. This solution is efficient and guarantees the correct functionality of the task requirement.