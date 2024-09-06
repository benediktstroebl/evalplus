Here is a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('')  # Output: 0
>>> strlen('abc')  # Output: 3
```

This function uses the built-in `len()` function to calculate the length of the input string. It then returns the receives a string as an argument and simply returns the length of that string using the `len()` function. The test cases validate the example usage of the `strlen()` function to ensure its correctness.