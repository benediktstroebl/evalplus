```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string
    
    Returns:
        str: The string with case flipped
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Testing the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # Expected output: 'hELLO'
    print(flip_case('hello'))  # Expected output: 'HELLO'
```

This script defines a function `flip_case` that uses a generator expression to iterate over each character in the input string, swap its case with `swapcase()`, and then join them all back into a single string. The `if __name__ == "__main__":` block is used to test the function by calling it with different inputs.