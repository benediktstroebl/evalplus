```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3
```
The function `strlen` calculates and returns the length of the given string. It takes advantage of the static `len()` function to get the length of a given string. The function is self-contained and has no external dependencies, passing all the tests successfully.