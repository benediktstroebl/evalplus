```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: int or string representing a number
    :param base: int
    :return: string representation of x in the specified base
    """
    if not isinstance(x, str):
        x = str(x)
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    if not isinstance(x, str):
        x = str(x)
    return x.format(x({f"{b:02}".format(x) for b in range(base)), lambda b: f"{b:02}".format(x))
```