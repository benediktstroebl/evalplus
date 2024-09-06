Here's the self-contained Python script with the function `strlen` that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('') # Should return 0
>>> strlen('abc')  # Should return 3
```

This function takes a string as input and returns its length using the built-in function `len()`. The test cases ensure that the function is working correctly by passing various inputs and verifying the returned values.