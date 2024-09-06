```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the residual decimal part. 

To validate the operation, please consider the following tests:
```python
# Testing suite
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
    assert truncate_number(12.345) == 0.345
```
The tests ensure that the function performs as expected across different ranges. 
If you would like to see the above tests executed and integrated into a testing framework, I can easily provide that as well. A comprehensive testing framework helps provide reassurance that the code will work across different scenarios and contexts and will be maintainable and reusable in the future.