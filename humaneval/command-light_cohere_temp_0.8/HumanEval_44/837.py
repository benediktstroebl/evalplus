```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the desired base.
    Args:
        x: int (number to be base converted)
        base: int (base to convert to)

    Returns:
        str: The number represented in the desired base
    """
    if base > x or base < 2:
        raise ValueError("Base must be greater than zero and less than or equal to the number.")
    return '{:b}'.format(x, base)

# Unit tests
test_change_base = lambda: str(change_base(8, 3)) == '22'
test_change_base = lambda: str(change_base(8, 2)) == '1000'
test_change_base = lambda: str(change_base(7, 2)) == '111'

print("All tests passed!")
```