```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)
```

This function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer to it (achieved using the int() function). This operation effectively separates the integer part of the decomposition and returns the remaining fractional part. 

To validate the functionality of this function, you can write a test case like this:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
```