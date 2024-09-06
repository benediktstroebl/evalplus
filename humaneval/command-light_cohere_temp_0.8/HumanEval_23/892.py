Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string"""
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3
```

This code defines a function `strlen` that calculates the length of a given string. The function uses the`len` to return the length of the input string.