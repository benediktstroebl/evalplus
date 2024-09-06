```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the decimal part of the number. 

To test this function, you can call it with a float input and assert that the result is less than 1:
```python
import numpy as np

truncate_number_tests = [
    (3.5, 0.5),
    (2.8, 0.1),
    (0.4, 0.4),
    (11.23, 0.23)
]

for number, expected in truncate_number_tests:
    assert truncate_number(number) == expected, f"For {number}, expected {expected}, but got {truncate_number(number)}."
``` 

This test suite covers a range of scenarios where the function should output the decimal part of the input number, and asserts that the output is as expected.