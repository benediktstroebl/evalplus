```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Should print: 0
print(strlen('abc'))  # Should print: 3
```

However, as per your request for a self contained solution, here is a reworked version of the script that has the tests (like doctests) built into it:

```python
import doctest

def strlen(string: str) -> int:
    """ Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

if __name__ == "__main__":
    doctest.testmod()
```

In this version, we use the `doctest.testmod()` function to run the tests defined in the docstrings of the functions in the script. If all tests pass, it will exit silently; otherwise, it will print the results of the failed tests and exit with a non-zero status code.