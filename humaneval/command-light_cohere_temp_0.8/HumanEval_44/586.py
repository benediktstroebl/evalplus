```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number 'x' 
    to the specified base 'base'.
    """
    if x < 0 or base < 0 or base < x:
        raise ValueError("Invalid arguments. Base must be greater than >= 0 and number > 0")
    # perform the conversion
    return format(x, base)
```