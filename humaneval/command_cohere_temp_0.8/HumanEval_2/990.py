```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 

To test this function, here is a test case:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.83) == 0.83
```

The tests ensure that the function correctly identifies the decimal part of different numbers. Feel free to add more tests to cover other scenarios.