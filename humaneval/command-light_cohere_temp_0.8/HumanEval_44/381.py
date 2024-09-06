```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    """ return string representation of x in the desired base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    return format(x, base)

x = 8
y = 3
z = 'a'

print(change_base(x, y)) # expected output: 22
print(change_base(z, 2)) # expected output: a
print(change_base(x, 2)) # expected output: 8
print(change_base(3, 4)) # expected output: 44
```