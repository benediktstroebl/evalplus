```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of x in the given base.
    """
    convertString = "0123456789"
    result = ''
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses a while loop to repeatedly divide the input number `x` by the base, appending the remainder to the result string. The remainder is obtained by taking the modulus of `x` with the base. The conversion string is used to map the remainders to their corresponding digits in the new base.