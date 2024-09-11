```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as an argument and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. 

The script also includes two test cases at the end to demonstrate the function's behavior. The expected output is provided in comments next to each test case.