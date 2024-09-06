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
    >>> change_base(10, 5)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(None), expected int()
    """
    # check if the number is not None
    if x is None:
        raise TypeError("Input number is None")

    # base conversion
    return format(x, base, signed=True)

# test the function with some edge cases
try:
    change_base(8, 3)
    print("Test passed")
except TypeError as e:
    print("Test failed:", str(e))
```