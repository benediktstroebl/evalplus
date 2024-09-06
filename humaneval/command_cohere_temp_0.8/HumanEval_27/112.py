```python
def flip_case(string: str) -> str:
    """
    Flip uppercase characters to lowercase and lowercase characters to uppercase.
    """
    flipped = ''
    for char in string:
        if char.isupper():
            flipped += char.lower()
        elif char.islower():
            flipped += char.upper()
        else:
            flipped += char
    return flipped
```
This version of the function focuses solely on the flipping behavior, avoiding the creation of an intermediate string for concatenation, and instead, using a building approach to directly construct the result.