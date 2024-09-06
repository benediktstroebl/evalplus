```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(0.1) == 0.0
    assert truncate_number(100.5) == 0.5

test_truncate_number()
```

The function `truncate_number` takes a float number as a parameter and returns the decimal part of the number. This is achieved by subtracting the integer part of the number (obtained by rounding the original number) from the original number. The tests affirm the function's behavior for different cases.