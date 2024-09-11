```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The length of the input string.
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3

print("Test cases passed.")
```

In this script, we define a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to calculate the length of a string. We include two test cases to verify the correctness of our function.

If you want to run this script and see the results, save it to a file (for example, `string_length.py`) and run it using Python (for example, `python string_length.py`). If the function is working correctly, you should see the output "Test cases passed."