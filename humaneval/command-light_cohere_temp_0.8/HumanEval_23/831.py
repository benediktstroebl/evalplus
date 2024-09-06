Here's the self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This function takes a string as input and returns its length using the `len()` function. It provides a general and clear documentation with a docstring that describes the purpose of the function and its usage.

You can use this function in your markdown code block to calculate the length of any given string.