### Change Numerical Base Script

```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to convert.
        base (int): The target base numbers. Must be less than 10.
    
    Returns:
        str: The string representation of the number in the target base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers")
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9")

    # Handle negative numbers
    if x < 0:
        sign = "-"
        x = -x
    else:
        sign = ""

    # Convert the number to the target base
    result = []
    while x:
        result.append(int(x % base))
        x //= base

    # Reverse the list and join it into a string
    result = sign + "".join(str(digit) for digit in reversed(result))

    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses a simple algorithm to convert the number to the target base. It uses the modulo operator (`%`) to get the remainder of the number divided by the base, and the floor division operator (`//`) to get the quotient. The result is a list of digits in the target base, which is then reversed and joined into a string. The script also handles negative numbers by storing the sign separately and removing it before converting the number.