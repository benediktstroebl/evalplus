```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to convert.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    
    # handle the special case when x is 0
    if x == 0:
        return "0"
    
    result = ""
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    return result


# Test cases
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: 22
    print(change_base(8, 2))  # Output: 1000
    print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that converts a number `x` from base 10 to another base. It uses the built-in `divmod` function to get the quotient and remainder of the division of `x` by `base`. The remainder is prepended to the result string. This process is repeated until `x` is 0. The function then returns the result string. The test cases at the end demonstrate the function's correctness.