```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: String representation of the number in the target base.
    """
    # Convert to base 10 if x is less than base
    if x < base:
        return str(x)
    
    # Initialize an empty string to store the result
    result = ''
    
    # Perform the conversion
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        # Prepend the remainder to the result
        result = str(remainder) + result
        # Update x to be the quotient of x divided by base
        x = x // base
    
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(5, 2))  # Output: '101'
print(change_base(10, 2))  # Output: '1010'
print(change_base(10, 8))  # Output: '12'
```
This code uses a while loop to repeatedly divide the input number by the target base, prepending the remainder to the result each time. The process continues until the input number is reduced to 0. The result is then returned as a string. If the input number is less than the target base, it is returned immediately as a string.