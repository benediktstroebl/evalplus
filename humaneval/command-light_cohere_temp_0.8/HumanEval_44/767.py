```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    If the base numbers less than 10.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    # Based on the choice of base, create the corresponding power of 10
    power = [10]
    while x > 0:
        x //= power[0]
        power.append(10)
    return x  # Return the number as a string
```