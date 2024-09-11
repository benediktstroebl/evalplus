```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target numerical base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `change_base` that converts an integer `x` from base 10 to a target base. It uses a helper string `convertString` to map the digits to their corresponding characters in the target base. The function uses integer division (`x // base`) and modulus (`x % base`) to extract the digits in the target base and recursively call itself until the input number `x` is less than the target base.