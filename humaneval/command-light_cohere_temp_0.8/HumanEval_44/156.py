```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are` 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 5) # 5 is not a base 2 number
    '05'
    >>> change_base('qaw', 5) # Alphabet not int or base 5
    'qaws'
    """
    return '{:04b}'.format(x, base)
```