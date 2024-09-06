```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: Empty string
assertEqual(strlen(''), 0)

# Test case 2: Single character
assertEqual(strlen('a'), 1)

# Test case 3: Two characters
assertEqual(strlen('ab'), 2)

# Test case 4: With spaces
assertEqual(strlen('   abc'), 3)
```  The code defines a function `strlen` that calculates the length of a given string. It uses the Python's `len()` function, which returns the length of the passed string. The test cases are then passed to the `assertEqual()` function to check the correctness of the `strlen()` function.