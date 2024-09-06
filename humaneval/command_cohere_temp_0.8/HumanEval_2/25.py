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
    (21.5, 1.5),
] 

for n, expected in test_cases:
    result = truncate_number(n)
    assert result == expected, f"For {n}, expected {expected}, but got {result}"
```
This will provide confidence that the function performs as expected.