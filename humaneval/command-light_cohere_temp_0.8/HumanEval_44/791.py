```python
def change_base(x: int, base: int) -> str:
    """Change the base of a number x to base base b.
    Raise a string representation
   
    >>> change_base(8, 3)  # => '22'
    >>> change_base(10, 2)  # => '1000'
    >>> change_base(7, 2)  # => '111'
    """
    if base == x % base:
        return f'{x}'
    else:
        return str(x)
```