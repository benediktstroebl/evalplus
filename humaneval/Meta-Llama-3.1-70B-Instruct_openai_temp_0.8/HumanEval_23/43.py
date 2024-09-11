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

# Test the function
assert strlen('') == 0
assert strlen('abc') == 3

print("All tests passed")
```