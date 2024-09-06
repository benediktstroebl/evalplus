```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the result. 

Here is a test case to verify its functionality:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(1.0) == 0.0
```