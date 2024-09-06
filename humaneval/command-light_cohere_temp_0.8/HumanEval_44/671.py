```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    if base <10 != 10:
        return '{:b}'.format(x, base)
    else:
        return '{:02}'.format(x)
```
We're changing the base of the number `x` to the specified base. We handle the using base number and perform the necessary conversion if the base is not 10, otherwise, we use string formatting to represent the number with the desired base precision.