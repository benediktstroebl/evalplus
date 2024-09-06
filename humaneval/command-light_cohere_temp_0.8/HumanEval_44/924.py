Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are
    uses base 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('123', 5)
    Traceback (most recent call last):
      File "<string>", line 10: in <module>:\nchange_base()
    File "<string>", line 19: TypeError: 'int' object does not support item assignment

Error:

The provided function is not fully self-contained and does not pass all the tests.

Let me help you to improve the code and fix the issues.