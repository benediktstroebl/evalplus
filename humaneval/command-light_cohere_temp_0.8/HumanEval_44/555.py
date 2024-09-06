```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer x to the base B.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(7, 0)
    Traceback (most recent call last):
    TypeError: unsupported operand type(7) for +() with int()
    False
    """
    # Make sure base is a number and x is an integer
    if not isinstance(base, (int, float)) or not isinstance(x, int):
        raise TypeError("Invalid arguments. Input must be numbers.")
    
    # Implement the decimal to base conversion
    # Use string formatting to get decimal number with required base
    result = '{:.1f}'.format(x, base)
    return result
```  This code defines a function called `change_base` that takes two arguments: `x`, which is the number to be converted, and `base`, which is the desired base. The function checks the goal is to convert a number `x` into a string in a base `base` and raise a `TypeError` if `base` or `x` is not a valid number. The function then performs the string formatting on `x` with `base` to convert it into a string representation using the specified base. The resulting string is then returned.