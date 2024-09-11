### Change Numerical Base of Input Number
#### Python Script
```markdown
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The target base.

    Returns:
        str: The string representation of x in the target base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers.")
    if 10 < base:
        raise ValueError("Base must be a number less than 10.")
    if x == 0:
        return '0'

    result = ''
    while x > 0:
        # get remainder of x divided by base
        remainder = x % base
        # add remainder to the result
        result = str(remainder) + result
        # update x to be quotient of x divided by base
        x = x // base

    return result


# Example usage
print(change_base(8, 3))  # prints: 22
print(change_base(8, 2))  # prints: 1000
print(change_base(7, 2))  # prints: 111
```
In this script we first ensure that both x and base are integers, and raise a ValueError if not. We also check if the base is less than 10. We then convert the number using a while loop, where we get the remainder of x divided by base, and update x to be quotient of x divided by base. We keep doing this until x is 0, at which point we have the result in the target base.