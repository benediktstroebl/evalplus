```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string input `s` and returns the length of that string. The function utilizes the built-in `len` function to calculate the number of characters in the input string. It then returns the length as an integer. 

The function is designed to address the problem of determining the length of a given string, as exemplified in the provided test cases. You can use it in your code to obtain the length of any string by calling `strlen` and passing the string as an argument. 

To execute the function, you can test it by calling `strlen` with different strings to verify its behavior. For instance:
```python
print(strlen("Hello, world!"))  # Output: 13
print(strlen(""))  # Output: 0
```

This will help you confirm that the function behaves as expected, returning the length of the corresponding input string. Feel free to test it with other strings to validate its behavior fully.