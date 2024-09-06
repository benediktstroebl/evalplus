```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base base.
    Return string representation after conversion.
    base numbers other for 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('123', 1)
    Traceback (most recent call last):
      File "<user_input>", line 8, in <module>
    ValueError: 'str()' object does not support item assignment: '123'
    """
    return str(x)
```