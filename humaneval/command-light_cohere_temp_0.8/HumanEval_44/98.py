```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are required 10
   
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 5)
    Traceback (most recent call last):
      File "<filename>", line 10, in <module>
    AssertionError: incompatible types: int() != str()
    """
    return str(x)
```