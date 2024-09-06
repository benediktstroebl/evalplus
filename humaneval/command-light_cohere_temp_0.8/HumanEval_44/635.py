```python
def change_base(x: int, base: int) -> str:
    """Change the base numerical representation of input number x to base base.
    Return a string representation after conversion.
    base numbers less 10
   
    """
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return format(x, f"{base}"))
```