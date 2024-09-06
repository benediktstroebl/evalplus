```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. When the character is alphabetic, it uses the `swapcase()` method to flip between uppercase and lowercase. Non-alphabetic characters are appended as is. The output will be the input string's characters flipped as described in the problem statement.