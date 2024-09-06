```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    Returns a string representation after conversion.
    base numbers less 10
    support.
    >>> change_base(8, 3)  # => '22'
    >>> change_base(8, 2)  # => '1000'
    >>> change_base(7, 2)  # => '111'
    """
    return '{:0b}'.format(x, base)
```