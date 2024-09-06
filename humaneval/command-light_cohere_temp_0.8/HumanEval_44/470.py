```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number x to base base.
    return string representation after conversion.
    base numbers less 10
    this common base numbers.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 5)
    Traceback (most recent call last):
      File "<stdin>", line 20, in <module>
    AssertionError: '9' not in ['2', '8', '10']
    ```