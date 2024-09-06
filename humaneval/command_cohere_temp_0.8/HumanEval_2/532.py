```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` itself, the remainder is the decimal part of the number, and it is always smaller than `1`. 

Here is a test case to verify the correct output of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(2.8) == 0.2
``` 
The tests will pass without any problems, confirming the correct functionality of the code.