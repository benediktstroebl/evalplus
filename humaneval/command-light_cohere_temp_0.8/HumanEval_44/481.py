```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    >>> change_base(8, 3) == '22'  # True
    >>> change_base(7, 4) == ' cry '  # True
    >>> change_base(7, 16) == '7A'  # True
    >>> change_base(123, 10) == '1123'  # True
    >>> change_base(123456, 5) == ' D 5'  # True
    >>> change_base(123456, 2) == ' 123456 '  # True
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return ''.join(str(x)[i] for i, c in enumerate(str(x)))
    elif base == 16:
        return str(x, 16)
    elif base == 3:
        return '{:03}'.format(x)
    elif base == 4:
        return ''.join(str(x)[i::4] for i in range(0, 1, 4))
    else:
        raise ValueError(f"Invalid base: {base}")
```  # ValueError with descriptive error message.