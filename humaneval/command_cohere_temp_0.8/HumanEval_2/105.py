```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the residual. 

You can test this function against the provided `test_truncate_number` block to verify its correctness. 
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(0.4) == 0.0
    assert truncate_number(101.101) == 0.101
``` 
This test suite will verify the correctness of the solution for different input scenarios.