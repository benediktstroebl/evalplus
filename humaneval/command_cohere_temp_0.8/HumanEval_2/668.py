```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which inherently removes the largest integer part and leaves behind the residual fractional part. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_output
```
This will assert the result is `0.5`.