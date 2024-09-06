```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    Convert x to a string representation in the given base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(128, 4)
    Traceback (most recent call last):
      File "<stdin>", line 3, line 3: TypeError: unsupported operand type(128)
    """
    # handle invalid base
    if base < 2 or base > 36:
        raise TypeError("Invalid base, base must be between 2 and 36.")
        
    result = bin(x)[base-2:].zfill()
    return result
```