```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.
    """
    return len(string)
```
The function directly uses the built-in `len()` function of Python to get the length of any given string. This function works for empty strings as well as any other normal string.
```python
# Tests
assert strlen("") == 0
assert strlen("abc") == 3
```