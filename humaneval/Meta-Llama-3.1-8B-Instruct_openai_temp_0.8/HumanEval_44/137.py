```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The base to convert the number to.
    
    Returns:
        str: The string representation of x in base.
    """
    convertString = "0123456789ABCDEF"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base number `base` as inputs. It uses a while loop to continuously divide the input number `x` by the base until `x` becomes 0. The remainder of each division is appended to the result string. The base is used to determine the character to append to the result string. The convertString is used to map the base values to their corresponding characters. 

Please note that for base above 10, the convertString should be extended to include more characters. For bases above 16, you might need to define a larger string.