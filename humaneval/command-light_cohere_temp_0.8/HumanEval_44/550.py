```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    Args:
        x: int or string, number to be converted
        base: int, the base to which the conversion will be performed.
    Returns: string representation of x in the given base.
    """
    take the example:
    >>> change_base(8, 3)
    '22'
    >>> change_base('8', 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if isinstance(x, str):
        x = int(x)
    return format(x, '{base}', int(x))

``` 
The provided code defines a function called `change_base` which takes two arguments: `x` (either an integer or a string) and `base` (the base to which the conversion will be performed). The function converts the input `x` to a string using `format`, then formats it using the specified base. The function then returns the string representation of `x` in the given base.