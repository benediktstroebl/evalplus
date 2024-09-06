```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns the string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 5)
    TraceError: incompatible argument types
    """
    try:
        return str(x) if x <= len(str(x)) and base <= 5 else "TraceError: incompatible argument types"
    except TypeError:
        return "TraceError: unexpected value"

```