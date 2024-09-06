```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the desired decimal part. 

Here is a test case to test the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.8) == 0.8
    assert truncate_number(2.0) == 0.0
``` 
This test case ensures that the function 'truncate_number' returns the correct value for different inputs. 

 disclaims liability for any consequences resulting directly or indirectly from any action or inaction taken based on the information provided.