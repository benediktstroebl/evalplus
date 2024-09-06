```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: int or number to be base changed
    :param base: new base to which the number will be converted
    :return: string representation of the number
    """
    # Raise error if invalid arguments are passed
    assert isinstance(x, int) and x >= 0 and base >= 2 and isinstance(base, int), "Invalid argument types or values!"
    assert x <= len("{:b}".format(str(x))) // base
    return "{:b}".format(x, base)

# Test the function
x = 8
print(change_base(x, 10))  # Expected output: 22
x = 8
print(change_base(x, 2))   # Expected output: 1000
x = 7
print(change_base(x, 10))  # Expected output: 177
```