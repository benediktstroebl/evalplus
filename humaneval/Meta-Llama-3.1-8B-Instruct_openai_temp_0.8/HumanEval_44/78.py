```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to convert.
    base (int): The base to convert to (less than 10).
    
    Returns:
    str: The string representation of the number in the new base.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    if x == 0:
        return "0"

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return "".join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script includes the `change_base` function with a docstring explaining its behavior. It also includes a `while` loop that continuously divides the input number by the base until it reaches zero, appending the remainder to the `digits` list. The result is then constructed by joining the digits in reverse order. The test cases are included at the end to demonstrate the function's behavior.