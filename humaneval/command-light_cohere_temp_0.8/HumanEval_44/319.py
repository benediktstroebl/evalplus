```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a given number to a specified base.
    """
    converts the scenario to string representation.
    base numbers under 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return '{}'.format(x, base)
```