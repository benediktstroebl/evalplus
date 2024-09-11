```python
def strlen(string: str) -> int:
    """
    Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
import doctest
doctest.testmod()
```

This script uses Python's built-in `len()` function to calculate the length of a string. It also includes test cases using Python's `doctest` module to verify the correctness of the `strlen()` function.