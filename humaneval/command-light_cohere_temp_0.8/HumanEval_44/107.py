```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to the specified base, and returns the string representation.
    """
    base numbers are 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 1)  # Example with invalid base
    '05'
    >>> change_base(5, 'abc') # Example with invalid base
    '05abc'
    """
    if base > 0 and base <= 36:
        return f'{x}'[(base - 1) : base]
    else:
        return 'Invalid base'
```