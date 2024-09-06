```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert uppercase characters to lowercase and vice versa. The isalpha function is used to determine if a character needs to be flipped. The join function is then used to combine all characters into one string. This solution works for both alpha and alphanumeric strings.