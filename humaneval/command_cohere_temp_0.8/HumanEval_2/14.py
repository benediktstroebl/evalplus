```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` returns the decimal part of the input number by subtracting the largest integer less than or equal to the number from the number itself. This effectively removes the integer part of the number, leaving only the decimal part. 

To test this script, you can create a test case like the one provided in the original description:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.2) == 0.2
    assert truncate_number(101.1) == 0.1
```

This would verify that the function behaves as expected for a few different input numbers. 

Please note that the function assumes that the input number is a valid floating point number, and that the integer part of the number is representable as an integer. If the input number is not well-formed, the function may return unexpected results.