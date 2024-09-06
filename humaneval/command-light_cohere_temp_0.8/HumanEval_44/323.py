```python
def change_base(x: int, base: int) -> str:
    """Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are particular 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 5) # incorrect base, should return error string
    TraceError: float '123': invalid literal for int()
    """
    return str((x if x <= base else 'invalid') )
```