```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    """
    base must be a power of 10, and must not be 0.
    """
    if base <= 0 or raise ValueError("base must be a positive integer")
    
    return "{:b}".format(x, base)
```