```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case that verifies the correct operation of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.83) == 0.83
    assert truncate_number(123.456) == 0.456
    assert truncate_number(0.514) == 0.014
```