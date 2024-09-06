```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(3, 1)
    Traceback (most recent call last):
      File "<stdin>", line 1, error=sys.asiserror:
    ValueError: unsupported operand type(3) for +)'
    """
    return f"{x:.{{base}"}
```