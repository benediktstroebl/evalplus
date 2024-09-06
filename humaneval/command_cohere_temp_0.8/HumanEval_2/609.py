```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the leftover decimal amount. 

You can test this function using the following code: 
```python
# Test the function with a sample input and expected output
test_case = [3.5, 0.5]
assert truncate_number(*test_case) == test_case[1]
```
This would test the function with the sample input of 3.5 and the expected output of 0.5, which should evaluate to true if the function is working as expected.