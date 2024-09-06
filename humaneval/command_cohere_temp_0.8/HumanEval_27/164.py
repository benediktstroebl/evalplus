```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)
```

This code uses a list comprehension to iterate through each character in the input string. For alpha characters, it uses the `swapcase()` method to flip between uppercase and lowercase. Non-alpha characters are directly appended to the resulting string. This ensures that only alphabetic characters are flipped while leaving non-alphabetic characters unchanged.