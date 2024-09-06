```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, which yields the decimal part, then returns the decimal part as the result. 

Here is a test case that can be used to verify the functionality of the code:
```python
test_case = 3.5
expected_result = 0.5

result = truncate_number(test_case)

assert result == expected_result
```