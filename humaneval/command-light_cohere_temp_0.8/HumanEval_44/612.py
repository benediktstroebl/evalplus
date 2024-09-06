```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the specified base.
    Test if x is numeric, raise ValueError.
    if base <0 ors a number of digits or is negative, raise ValueError.
    return ''.join(x, int(x))
    """
    if not isinstance(x, str):
        raise ValueError("Input should be a string representing a number")
    if len(x) == 0:
        raise ValueError("Input cannot be an empty string")
    if base < 0 or base > 20:
        raise ValueError("Base must be between 1 and 20")
    try:
        return ''.join(x, int(x))
    except ValueError as e:
        raise ValueError(str(e))
```