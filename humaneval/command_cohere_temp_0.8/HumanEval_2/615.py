```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the result. The integer part of a number can be found using the `int()` function. 

Here is a test case that can be used to validate the functionality of the function:
```python
test_case = 3.5
expected_result = 0.5
result = truncate_number(test_case)

assert result == expected_result
```
The test case ensures that the function returns the correct decimal part of the input `number`. 
It can also be used for testing the function for any edge cases that might arise in the future, as it solely depends on the decimal part of the number, while the integer part remains constant.