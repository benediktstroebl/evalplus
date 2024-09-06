```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base,
    and return the string representation.
    """
    specific bases that are 10, 2, and 2 in decimal system
    """
    if base not in [10, 2, 2]:
        raise ValueError("Invalid base. Use 10, 2, or 2")
    return format(x, base)
```