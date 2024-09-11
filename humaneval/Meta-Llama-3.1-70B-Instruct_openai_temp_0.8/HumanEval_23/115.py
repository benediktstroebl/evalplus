```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the input string
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3

print("All test cases pass")
```

This Python script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. It also includes two test cases to verify the correctness of the function. If the function works as expected, it will print "All test cases pass".