```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> changebase(8, 2)
    '1000'
    >>> changebase(7, 2)
    '111'
    >>> changebase(12, 10)
    Traceback (most recent call last):
      File "<stdin>", line 5, in <module>
    ValueError: unsupported operand type(12, 'int'), expected ('int', 'str')
    """
    # handle invalid input
    if isinstance(x, str) and x.base not base:
        raise ValueError("Input should be a valid base number or a string.")
    elif base <= 0:
        raise ValueError("Base number should be positive.")
    else:
        # convert to string and back to int
        base_str = str(base)
        x_str = str(x)
        return int(base_str + x_str[::-1])
```