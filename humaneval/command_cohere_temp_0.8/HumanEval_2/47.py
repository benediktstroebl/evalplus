```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual value. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_result = 0.5

result = truncate_number(test_truncate_number)
assert result == expected_result
```

The test code checks if the result of the function corresponds to the expected result. 
This is done by creating a test case with a sample input and a expected output and then running the function in the debugger, where it will stop and ask you to confirm every step to make sure that it is operating as expected. 
If the outputs correspond to the expected outputs, then the test will be successful; otherwise, it will be considered a failure.