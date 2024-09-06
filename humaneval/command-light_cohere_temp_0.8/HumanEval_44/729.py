```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number 'x' to the specified base.
    Returns the string representation after conversion.
    base numbers are maximum 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 60)  # Should raise error
    TraceError: metring 'invalid literal for int()': ' ' '
    """
    # Convert x to string and convert to base base
    return '{}'.format(x, base)
```