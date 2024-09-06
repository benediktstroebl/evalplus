```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the residual fraction. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_output
```

The test will pass as the expected output was calculated correctly. 
Please let me know if you would like me to explain any parts of the code in more detail.