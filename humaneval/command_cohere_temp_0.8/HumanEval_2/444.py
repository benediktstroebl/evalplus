```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is achieved by finding the difference between the number and the closest integer using the `int()` function which returns the closest integer to the given number. 

Here are some tests that can be run to ensure the function is working as expected:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.899) == 0.099
    assert truncate_number(0.0) == 0.0
    assert truncate_number(56.0) == 0.0
    assert truncate_number(1.0001) == 0.0001
```