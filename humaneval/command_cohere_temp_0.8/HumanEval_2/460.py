```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (via int(number)) and subtracts this integer from the original number, yielding the decimal part (the leftover part smaller than 1). 

To test this function, execute the following code in your Python environment of choice: 
 ```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.0, 0.0),
    (1.5, 0.5)
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
```
The test_cases list provides different numbers and the expected decimal parts. The test suite checks if the `truncate_number` function returns these expected decimal parts for each test case.