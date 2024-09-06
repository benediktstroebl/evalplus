```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as input and returns the decimal part of the number by simply subtracting the integer part of the number (obtained by converting it to an integer).

Here's a test case to verify the functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(1.0) == 0.0
```