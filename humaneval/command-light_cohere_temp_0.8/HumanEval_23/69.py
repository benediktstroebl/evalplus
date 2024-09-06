Here is a self-contained Python function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test case for empty string
assert strlen('') == 0

# Test case for non-empty string
assert strlen('abc') == 3
```
This code defines a function `strlen` that calculates the length of a given string, and passes the tests successfully.