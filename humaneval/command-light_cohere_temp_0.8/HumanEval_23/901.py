Here's the code you asked for:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
```
This code defines a function `strlen` that calculates the length of a given string.  It takes a this method, it simply uses the built-in `len()` function to get the length of the passed string, and the test cases ensure the correctness of this function.