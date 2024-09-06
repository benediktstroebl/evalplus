Here is a self-contained Python script that solves the problem of checking for elements in a list that are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any(abs(num1 - num2) <= threshold for num1, num2 in numbers)
    return True
```
This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the given threshold. 

The function uses the `any` function to check if there exists a pair of numbers in the list that their absolute difference is less than or equal to the given threshold.