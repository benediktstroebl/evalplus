```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    Parameters:
        x: int or string, base: int
    Returns:
        str: string representation of x with base b
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Invalid input types. Input should be an string or base of form 10 or int.")
    return format(x, base)
```