```python
def change_base(x: int, base: int):
    """Change the base of the input number x to base base.
    If return a string representation after conversion.
    base numbers 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return format(x, f"{base}eliB")
```