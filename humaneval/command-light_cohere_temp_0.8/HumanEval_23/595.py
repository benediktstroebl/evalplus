Here is a self-contained Python script that defines a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''),     0)
assertEqual(strlen('')),  0
assertEqual(strlen('abc')), 3
assertEqual(strlen(''''')), 4
assertEqual(strlen(' Toulbat')), 9
```

This code defines a function `strlen` that calculates the length of the given string using the `len()` function. It returns an integer value representing the past the length of the string.