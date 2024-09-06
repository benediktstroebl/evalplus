```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual decimal part. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

actual_output = truncate_number(test_truncate_number)

assert actual_output == expected_output
```
The provided code passes this test and should reliably capture the decimal part of a given number. 
It's a straightforward approach that accomplishes the goal and captures the residual decimal part of the provided number. 
It does not rely on any specific number of decimals or rounding conventions, making it adaptable to different scenarios and edge cases. 
However, if you were interested in maintaining the same decimal precision or rounding behavior, additional adjustments would be necessary.