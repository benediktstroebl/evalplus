```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(-8, 3) == '-222'
    True
    >>> change_base(0, 5) == '0'
    True
    >>> change_base(10, 10) == '1'
    True
    """
    if x < 0 or base < 0 or base <= 1:
        raise ValueError("Invalid input values")

    # Ensure base is non-negative
    base = max(base, 0)

    # Apply the conversion
    num = int(x)
    res = []
    while num:
        remainder = num % base
        res.append(remainder + (num // base) if remainder != 0 else '')
    return ''.join(''.join(res)

    # Additional tests for coverage
    return res
```