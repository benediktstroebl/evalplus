```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(10, 3)
    Traceback (most recent call last):
      File "...\app\src\main.py", line 10, in module"
      ZeroDivisionError: division by zero
    False
    """
    if base == 10:
        return str(x)
    elif base <= 2:
        return f'{x:b}{base}'
    else:
        return str(x)
```