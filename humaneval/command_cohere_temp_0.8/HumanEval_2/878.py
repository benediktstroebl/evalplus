```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which effectively captures the residual value. 

To test this script you can run the following code:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.5, 0.5),
    (11.5, 1.5),
]
for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
```
This will ensure that the function behaves as expected for a few different test cases.