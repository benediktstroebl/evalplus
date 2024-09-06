```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    Return string representation.
    """ Numbers from 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 5)
    TraceTypeError: unsupported operand type: '123'
    >>> change_base('abc', 35)
    TraceTypeError: unsupported operand type: 'abc'
    """
    raise TypeError("Unsupported operand type. Please provide int, not str, or float")
```