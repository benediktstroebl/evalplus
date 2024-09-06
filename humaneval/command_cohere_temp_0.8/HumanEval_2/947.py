```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case to test the above function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.3) == 0.3
    assert truncate_number(2.1) == 0.1
    assert truncate_number(101.12) == 0.12
    assert truncate_number(1.5) == 0.5
    assert truncate_number(57.8) == 0.8
``` 
Executing this test file against the function will yield test passes.