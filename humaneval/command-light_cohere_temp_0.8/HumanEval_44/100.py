```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    False
    """
    if base > x or base < 2 or base <= 0:
        raise ValueError("Invalid base value")
    return format(x, base)
```  This Python code defines a function named `change_base` that converts a given number `x` to a string representation in the specified base. The code raises a error for invalid base values and provides informative feedback. It follows the testing if the example calls for valid and invalid inputs.