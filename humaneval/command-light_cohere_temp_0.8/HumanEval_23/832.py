```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
# returning 0 for empty string
print(strlen(''))

# returning length for different strings
print(strlen('abc'))
print(strlen('   ''\t  '))
print(strlen('Python'))
```