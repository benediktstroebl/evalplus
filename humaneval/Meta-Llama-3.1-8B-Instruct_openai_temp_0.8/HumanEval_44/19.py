### Change Base Function
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base (less than 10).
    
    Returns:
        str: The string representation of the number in the target base.
    
    Raises:
        ValueError: If the base is not less than 10 or not an integer.
    """
    if not isinstance(base, int) or base < 2 or base >= 10:
        raise ValueError("Base must be an integer less than 10.")

    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    # Reverse the list of digits
    digits = digits[::-1]

    # Convert the list of digits to a string
    return ''.join(str(digit) for digit in digits)


# Example use cases:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This script implements the `change_base` function as described in the problem. It uses a while loop to divide the input number by the target base, appending the remainder to a list of digits. The list of digits is then reversed and converted to a string using a generator expression.