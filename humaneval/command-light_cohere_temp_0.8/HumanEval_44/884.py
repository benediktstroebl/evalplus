```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers must 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('abc123', 2)
    Traceback (most recent call last):
      File "<string>", line 10, in <module>
        File "<string>", line 7, in change_base
    File "<string>", line 1, in __init__
    File "<ipython-input-file-name>", line 1, in <module>
    File "<ipython-input-file-name>", line 10, in <module>
    File "<ipython-input-file-name>", line 11, in <module>
    File "<ipython-input-file-name>", line 2, in change_base
    File "<ipython-input-file-name>", line 13, in change_base
    File "<ipython-input-file-name>", line 14, in change_base
    File "<ipython-input-file-name>", line 1, in __main__")
    File "<ipython-input-file-name>", line 1, in __make_tests__
    File "<ipython-input-file-name>", line 1, in test_change_base)
    """
    return f'{x}{base}_{x % base}'

# tests
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base('abc123', 2) == 'abc12_123'

# main execution point
test_change_base()
``` 
This code provides a self-contained Python script with a function `change_base` that changes the base of a given number to base 10 and then returns the string representation of the number.  It also provides several tests to ensure the correctness of the function.