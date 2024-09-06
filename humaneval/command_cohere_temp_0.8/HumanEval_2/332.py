```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the total number, thus leaving only the decimal part as requested. The test for this function would be:
```python
test_number = 3.5
test_result = truncate_number(test_number)

assert test_result == 0.5
``` 

The `assert` statement will return the test result, which can be either `True` or `False`, indicating if the test passed or not. 
If the outcome of the operation is `True`, the test has passed. If it's `False`, the test has failed, indicating that the function may not be operating corrrectly.