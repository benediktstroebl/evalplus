```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses a list comprehension to iterate through each character in the input string. When it encounters an alphabetic character, it uses the `swapcase` method to flip between uppercase and lowercase. All non-alphabetic characters are left unchanged. This results in the desired effect of flipping the case of alphabetic characters.