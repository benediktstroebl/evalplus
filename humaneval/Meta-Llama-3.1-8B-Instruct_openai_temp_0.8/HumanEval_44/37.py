```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base for the conversion.
    
    Returns:
    str: The string representation of x in base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # Outputs: 22
print(change_base(8, 2))  # Outputs: 1000
print(change_base(7, 2))  # Outputs: 111
```

This script defines a recursive function `change_base` to convert a given number `x` from its decimal (base-10) representation to a target base. The base must be less than 10 since bases greater than or equal to 10 would not have a single-digit representation for all numbers.

The function uses integer division (`//`) to find the quotient and modulus (`%`) to find the remainder when dividing the number by the target base, effectively achieving recursive division. This process is repeated until the number is less than the target base, at which point it is converted to a string and prepended to the result of the recursive call.