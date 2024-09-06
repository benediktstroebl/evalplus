Here's the code to help you create a Python script that provides a self-contained function with a docstring and passes the tests:
```python
def strlen(string: str) -> int:
    """ Return length of given string, not empty.
    Args:
        string: str
    Returns:
        int
    """
    if not string:  # Empty string handle
        return 0
    return len(string)
```