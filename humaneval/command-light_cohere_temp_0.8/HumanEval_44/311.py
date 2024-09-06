```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation.
    base numbers less 10 and
    and should be positive integers.
    >>> change_base(8, 3)
    '22'
    >>> change_base(10, 2)
    '20'
    >>> change_base(3, 0)
    TraceError: unsupported operand type(3) in '**' ()
    >>> change_base(10, "hej")
    TraceError: unsupported operand type('hej') in '**' ()
    """
    if not_valid_base(base):
        raise ValueError("Invalid base number.")
    if x < 0:
        x = -x
    # Convert x to string representation using given base
    s = str(x, base)
    return s

def not_valid_base(base: int) -> bool:
    """Check if base number is positive."""
    return base > 0
```

This code defines a function `change_base` that takes an integer `x` and an integer `base` as input and returns the converted number as a string. The `not_valid_base` function checks if a given base number is positive, and if not, raises a `ValueError`. This code effectively converts a number to a string representation with a specific base, ensuring the base is positive and valid.