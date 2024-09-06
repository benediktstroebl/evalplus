```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number itself. The decimals left in the difference will be less than 1, representing the desired decimal part of the number. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

actual_output = truncate_number(test_truncate_number)

assert actual_output == expected_output
```
The test code checks if the output of the function is equal to the expected output when giving the test_truncate_number as an input.