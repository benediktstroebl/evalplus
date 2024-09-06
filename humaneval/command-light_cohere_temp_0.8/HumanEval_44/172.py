```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number 'x' to the base 'base'.
    """
    return f'{x:{base}'
    if base == 10:
        return str(x)
    return '{x:b}'  # use built-in 'int()' function to convert to string and add base prefix
```
The function takes an integer `x` and an integer `base` as input, and returns the string representation of `x` in the specified base.