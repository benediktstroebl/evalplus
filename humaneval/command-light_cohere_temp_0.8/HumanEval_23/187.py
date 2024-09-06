Here's the self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1: empty string
assertEqual(strlen(''), 0)

# Test case 2: one letter string
assertEqual(strlen('abc'), 3)
```
The `strlen()` function calculates the length of the passed string using the `len()` built-in function. The test cases demonstrate the expected behavior of the function.