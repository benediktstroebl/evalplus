```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. When encountering alphanumeric characters, it uses the `swapcase()` method to flip between uppercase and lowercase. Meanwhile, non-alphanumeric characters are appended to the result string unchanged. This ensures that punctuation, digits, and other non-alphabetic characters retain their original format.