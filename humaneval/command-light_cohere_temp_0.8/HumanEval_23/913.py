Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This code provides a function `strlen` that takes a string as input and returns its length. The function is self-contained, and the test cases pass the expected output.