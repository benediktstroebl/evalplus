```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. When encountering alphabetic characters, it uses the `swapcase` method to flip the case, while non-alphabetic characters like punctuation marks or spaces are retained in their original form. This method efficiently solves the problem without the need for additional characters to be included in the string.