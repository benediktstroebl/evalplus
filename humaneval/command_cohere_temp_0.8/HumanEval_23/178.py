```python
def strlen(string: str) -> int:
    """ Returns the length of a string. """
    return len(string)
```

This Python script provides a function (`strlen`) that takes a string as an argument and returns its length. The function leverages the `len()` function, which is a built-in Python function that returns the number of items in a container, such as the number of characters in a string. 

To validate the correctness of this function, two test cases are provided:
1. When an empty string is passed to the function, the return value should be 0.
2. When the function is given a non-empty string (e.g., "abc"), the expected output is the number of characters in that string, which is 3.

These test cases help confirm that the `strlen` function is operating as expected, providing a reliable means of determining the length of any given string.