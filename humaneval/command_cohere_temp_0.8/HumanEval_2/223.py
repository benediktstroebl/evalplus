```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the given floating point number and the nearest integer, which represents the decimal part of the number. 

To test this script, you can create a test case like this:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
``` 

The assert statements will check if the output of the truncate_number function corresponds to the expected decimal part of the number. 
If all the assert statements pass, then the test suite will succeed.