```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently removes the integer part of the number and leaves behind the residual decimal part. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_output
```
This will assert the expected output of the function against its test case.