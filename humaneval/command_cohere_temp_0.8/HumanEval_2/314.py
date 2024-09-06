```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently truncates the number to its decimal part. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

actual_output = truncate_number(test_truncate_number)

assert actual_output == expected_output
```

The test code checks if the output of the function corresponds to the expected decimal part of the number, which it does in this case. 
The output of this test would be `True` since the expected and actual output values are equal.