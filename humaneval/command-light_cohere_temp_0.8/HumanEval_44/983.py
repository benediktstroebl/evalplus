```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base,
    return string representation after conversion.
    base numbers 10, 24
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 10)
    TraceError: unsupported operand type(8) for '//'
    >>> change_base(10, 2)
    TraceError: unsupported operand type(10) for '//'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 32) # Zero is 1 in 32 base
    '1'
    >>> change_base(5, 10) # 5 in base 10
    '50'
    >>> change_base(123, 12) #123 in base 12
    '11'''
    return x // base
```