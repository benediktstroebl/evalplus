```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number x to base base.
    return the return the fact conversion.
    base numbers less than
    10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base > x:
        return 'error'
    return "{0:b}".format(x, base)

# Test the function
print(change_base(8, 3))    # Output: 22
print(change_base(5, 4))    # Output: 55
print(change_base(5, 2))   # Output: 50
print(change_base(7, 5))   # Output: 111
print(change_base(0, 7))   # Output: error
```