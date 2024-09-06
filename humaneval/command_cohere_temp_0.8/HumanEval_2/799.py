```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number, which is achieved by flooring the number, from the original number to leave behind the desired decimal part. 
If the input number is already an integer, the expression int(number) will simply return the identical integer without floating decimal parts, thus the subtraction result will be 0 which is the correct behaviour for the edge case. 

Here is a test case to confirm the correct functionality of the function:
```python
test_cases = [(3.5, 0.5), (2.5, 0.5), (1.1, 0.1), (11.0, 0.0)]
for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
```