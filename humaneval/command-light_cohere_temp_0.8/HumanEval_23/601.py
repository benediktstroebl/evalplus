```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Testing the function with known results
assertEqual(strlen(''),      # Zero-length string
               0)
assertEqual(strlen('abc')  # Single character string
               3)
assertEqual(strlen('abcabc')) # Double character string
               6)
assertEqual(strlen(''))     # Empty string
               0)
```