```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base, should be less than 10.
    
    Returns:
        str: The string representation of the number in the target base.
    
    Raises:
        ValueError: If base is not less than 10.
    """
    if base < 2 or base >= 10:
        raise ValueError("Base should be less than 10.")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while x:
        result = digits[x % base] + result
        x //= base
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function that converts a number from base 10 to a target base. It uses a while loop to perform the conversion and handles bases less than 10 by taking the remainder modulo the base and dividing the number by the base in each iteration. The converted number is then represented as a string using a string of digits, where the index of each digit corresponds to its value in the target base. The function raises a `ValueError` if the target base is not less than 10.