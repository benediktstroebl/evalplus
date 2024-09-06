```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are known from 2 to 36.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 43)
    Traceback (most recent call last):
      File "<stdin>", line 5, in <module>
    TypeError: unsupported operand type(0) for +() with 'base': int()
    ```