```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which yields the residual fraction. 

To test this script, you can run the following code: 
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.5, 0.5),
    (11.5, 1.5),
    (21.5, 1.5),
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
``` 

This will provide tests that ensure the function 'truncate_number' behaves as expected. 
If the script passes, then all tests will succeed and you will get an output similar to '>.+++.++.++++++.+++++.***********' (heart emoji indicates successful pass)