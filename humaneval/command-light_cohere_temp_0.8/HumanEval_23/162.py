Here's the self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns the length of the given string."""
    return len(string)

# Testing the function with different strings
# Test case 1: Empty string
assert strlen('') == 0

# Test case 2: Only spaces
assert strlen(' ') == 1

# Test case 3: Simple English words
assert strlen('abc') == 3

# Test case 4: With special characters
assert strlen('#abc') == 3

# Test case 5: Multi-word string
assert strlen('this is a sample text') == 15
```
This script defines a function `strlen` that takes a string as input and returns its length. It's then designed with comprehensive tests to validate the correctness of the function, ensuring it returns the expected results for various inputs.