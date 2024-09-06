```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are string is 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('abc123', 15)
    TraceError: invalid literal for argument of type 'str'
    """

    # Handle invalid input to avoid error
    x = str(x) if isinstance(x, str) else str(x)

    return format(x, '{!{}%b}b', int(base))
```