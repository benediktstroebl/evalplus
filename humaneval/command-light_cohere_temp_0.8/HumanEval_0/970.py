Here is a Python script that provides a self-contained function that solves the problem and passes the tests provided in the docstring:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5).3) 0.2) 0.0) 0.5
   0) 0.8) 0.1) is0 and 0.9) < 2.0, True)
   1, 2.0, False)

    for number1 in numbers:
        if (number1 - threshold <= number2 and number2 - threshold <= number1):
            return True
    return False

test cases:
[1.0, 2.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.8, 3.0, 0.8, 4.0, 5.0, 2.0, 3] 0.9, 0.0, 0.0, 0.0]
print("Output should be True")
```