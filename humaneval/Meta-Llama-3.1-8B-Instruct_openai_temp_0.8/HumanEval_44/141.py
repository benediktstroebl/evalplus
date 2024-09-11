```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    convertString = "0123456789"
    result = ""
    
    while x > 0:
        # Append the remainder to the result
        result = convertString[x % base] + result
        # Update x for the next iteration
        x = x // base
    
    return result

# Test the function
print(change_base(8, 3))  # Outputs: 22
print(change_base(8, 2))  # Outputs: 1000
print(change_base(7, 2))  # Outputs: 111
```

This script uses a while loop to continuously divide the input number `x` by the base until `x` becomes 0. The remainder of each division is appended to the result string in the order from least significant digit to most significant digit, thus reversing the order of the digits. The result string is then returned.

The `convertString` variable is a string of all the possible digits in the new base, which are numbers from 0 to 9, but this can be easily expanded to handle bases larger than 10.

The script ends with some test cases to ensure the function is working correctly.