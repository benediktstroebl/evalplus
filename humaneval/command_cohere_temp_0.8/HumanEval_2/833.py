```python
def truncate_number(number):
    """ Returns the decimal part of the number """
    return number - int(number)
```

To test the above function, a test case is provided below:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.71) == 0.71
    assert truncate_number(2.01) == 0.01
```