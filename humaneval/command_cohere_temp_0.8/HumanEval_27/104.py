```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert alphabetic characters to their flip case counterparts, while leaving non-alphabetic characters unchanged. It leverages Python's str.format syntax to create a concatenated string with the modified characters. The `isalpha()` method checks if a character is alphabetic, and the `swapcase()` method swaps the case of alphabetic characters. The result is a string with flipped case for alphabetic characters, while non-alphabetic characters remain unaffected.