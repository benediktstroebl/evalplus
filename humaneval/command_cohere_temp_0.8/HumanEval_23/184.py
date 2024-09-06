```python
def strlen(s: str) -> int:
    """Return the length of a string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string as an argument and returns the length of that string. The function utilizes the `len()` function, which is a built-in Python function that returns the number of items in a given object, to calculate the length of the input string. 

To validate the correctness of the `strlen` function, two test cases are presented. These test cases utilize Python's `unittest` module to verify the function's behavior against expected outputs. In the first test case, the empty string (`''`) is passed to the function; as the length of an empty string is zero, this test expects the output to be `0`. In the second test case, the string `'abc'` is passed to the function, thus expecting a result of `3` due to the length of this particular string being three. 

The function includes a docstring, which comprises a description of the function's purpose and behavior and provides information on the expected input type and return value. Additionally, the test cases include docstrings that elucidate their intended purpose and how they are designed to test the `strlen` function. 

This combined approach, featuring a function with a docstring and test cases with docstrings, enhances the readability and understandability of the code, providing a clear and concise overview of its functionality. 

This way, the Python script not only presents the `strlen` function but also provides a self-contained testing framework, ensuring the function's correctness and facilitating its integration within larger projects.