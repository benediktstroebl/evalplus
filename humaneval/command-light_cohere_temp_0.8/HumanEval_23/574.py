Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcde'), 6)
assertEqual(strlen('abcabc'), 6)
assertEqual(strlen('   abc def'), 9)
```
This code defines a function `strlen` that calculates the length of a given string using the `len()` function. The function returns an integer value of the string length.