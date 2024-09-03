```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test the function
>>> strlen('') # Output: 0
>>> strlen('abc') # Output: 3
>>> strlen('   ')
3
>>> strlen(' 123') # Output: 4
>>> strlen('') || '123' # This should return 6
```

This code defines a function `strlen` that calculates the length of a given string. The function returns an integer value representing the length. It takes an simple approach for any string, regardless of its content. The test cases verify that the `strlen` function is working as expected. The last test case with an empty string and a string with spaces ensures that the function correctly handles empty strings.