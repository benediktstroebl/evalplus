```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with various inputs
print(strlen('')) # Output: 0
print(strlen('abc')) # Output: 3
print(strlen(''))    # Attemted error: should be 0, but the function takes str object instead of string
```