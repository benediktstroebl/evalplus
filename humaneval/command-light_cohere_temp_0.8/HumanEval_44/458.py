```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the specified base.

    :type x : int
    : base : int
    """
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    return str(x)

x = 8
try:
    print(change_base(x, 10))
    print(change_base(x, 2))
    print(change_base(x, 13))
    print(change_base(x, 17))
except ValueError as e:
    print(e)
```