```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which inherently truncates the decimal part and returns it on its own. 

To test this script you can run:
```python
test_truncate_number = 3.5
expected_output = 0.5

result = truncate_number(test_truncate_number)

assert result == expected_output
```
The test code checks if the output of the function, when the input is `3.5`, is equal to `0.5`. The assertion passes as the outcome of the function is precisely `0.5`.  This testing process validates the functionality of the script.