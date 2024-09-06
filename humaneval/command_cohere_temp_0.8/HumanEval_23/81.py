```python
def strlen(s: str) -> int:
    """Return the length of a string."""
    return len(s)
```

This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function, to determine the number of characters in the string. 

This function is self-contained, meaning it does not depend on any external variables or functions other than those that are automatically provided or defined in the script. 

To pass corresponding tests, you can create test strings and pass them to the `strlen` function, and compare the returned values with the expected lengths. Here is an example:
```python
# Test the function with an empty string
assert strlen("") == 0

# Test the function with a non-empty string
assert strlen("abc") == 3
```

This way, you can verify that the `strlen` function returns the expected output for different test cases.  This approach allows the function to be easily reused and integrated into larger projects, making it more reliable and maintainable.