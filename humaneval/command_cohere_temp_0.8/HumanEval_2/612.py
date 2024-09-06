```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as input and returns the decimal part of the number by simply subtracting the integer part of the number (obtained by converting it to an integer).

Here's a test case to test the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.3) == 0.3
    assert truncate_number(2.1) == 0.1
    assert truncate_number(101.12) == 0.12
```