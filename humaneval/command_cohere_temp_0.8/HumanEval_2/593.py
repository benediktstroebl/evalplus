```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case to confirm the correct functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.3) == 0.3
    assert truncate_number(2.1) == 0.1
    assert truncate_number(101.12) == 0.12
``` 
This test case covers different scenarios of positive decimal numbers, ensuring that the function 'truncate_number' returns the correct decimal part for each input number.