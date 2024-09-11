```python
def strlen(string: str) -> int:
    """
    Returns the length of a given string.

    Args:
    string (str): The input string.

    Returns:
    int: The length of the input string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


# Test cases
if __name__ == "__main__":
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"

    print("All test cases pass.")
```

In this script, we define a function `strlen` that takes a string as input and returns its length using Python's built-in `len` function. The function is documented with a docstring that provides a description of what the function does, its parameters, and its return values. Additionally, it includes example usage of the function.

The script also includes two test cases that verify the correctness of the `strlen` function. The `if __name__ == "__main__":` block ensures that these test cases only run when the script is executed directly (i.e., not when it's imported as a module in another script). If all test cases pass, the script prints a success message.