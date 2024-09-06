```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the input `number` and returns the result, which is the decimal part of the number. 

Here is a test case to verify the correct output for the given input:
```python
test_case = 3.5
expected_result = 0.5
result = truncate_number(test_case)
assert result == expected_result
```