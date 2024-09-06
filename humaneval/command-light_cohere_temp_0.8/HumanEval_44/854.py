```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    >>> change_base(8, 3) == '22'
    """
    if base > x // base:
        raise ValueError("base must be less than logarithm of x to base")
    # Ensure base is a power of 10 (handle non-powers)
    while base <= 10:
        base *= 10
    # Adjust x to have correct base and ensure it's positive
    x = (x // base) * base
    return f"{x}"
```