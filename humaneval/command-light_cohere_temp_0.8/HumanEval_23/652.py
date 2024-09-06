Here's a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),            # None
    )
assertEqual(strlen('')),         # Empty string
    )
assertEqual(strlen('abc'),    # Single character
    )
assertEqual(strlen(' foil'),  # Contains non-alphanumeric characters
    )
assertEqual(strlen("python"),  # Contains uppercase and special characters
    )
```  It uses the built-in function `len(string)` to return the length of the given string. 

Note that this function can be easily incorporated into your Python projects as it is self-contained and does not require any external dependencies.