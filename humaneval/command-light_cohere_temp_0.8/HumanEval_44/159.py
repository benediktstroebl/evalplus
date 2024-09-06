```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(10, 10)
    False
    >>> change_base(10, 'x')
    Traceback (most recent call last):
      File "<stdin>", line 19, in <module>
    ValueError: unsupported literal for int(): 'x'
    """
    # Perform the conversion
    if base > 0 and base <= 36:
        result = f'{x}'
        while base > 0:
            if base % 2 == 1:
                result = chr(int(result, base)) + result
            base //= 2
        return result
    else:
        raise ValueError("Unsupported base number")
```