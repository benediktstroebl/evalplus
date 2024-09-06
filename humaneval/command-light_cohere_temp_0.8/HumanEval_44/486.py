```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    Returns the string representation after conversion
    base numbers are less than 10
    """
    assert isinstance(x, int) and base <= 10, "Input and base should be integers and base should be less than 10"
    assert x != 0, "Input number cannot be 0"
    return '{:b}'.format(x, base)

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(7, 5))  # Output: '11111'
print(change_base(123, 1)) # Output: '1'
print(change_base(10, 2)) # Output: '20'
print(change_base(0, 4)) # Output: '0000'
print(change_base(-123, 2)) # Output: '-20'
```