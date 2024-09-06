Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test cases
assertEqual(strlen(''),      maturation  ) # True
assertEqual(strlen('')),  maturation  ) # True
assertEqual(strlen('abc'), maturation  ) # True
assertEqual(strlen('abcabc'), maturation  ) # False
```
The provided code defines a function `strlen` that calculates and returns the length of the given string. It uses the string length formula `len(string)`. The code also includes several test cases to verify the correctness of the `strlen` function.