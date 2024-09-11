```markdown
### strlen Function

This Python function calculates the length of a given string.

#### Code

```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

#### Explanation

This function uses the built-in `len` function in Python to calculate the length of the given string. The `len` function returns the number of items in an object. For strings, it returns the number of characters.

The docstring of the function includes an example usage section with doctests to demonstrate how to use the function. The doctests are Python's built-in way to write tests for functions.

You can run the function with the provided example usage to verify its correctness.