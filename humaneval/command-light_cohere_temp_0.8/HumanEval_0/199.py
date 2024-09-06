Here is a self-contained Python script that solves the problem of finding if any two numbers in a list are closer to each other than a given threshold:

```python
from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3, 0.1, 4, 0.8, 0.0, 2.0, 0.8, 0.0, 4, 5, 8, 3, 2, 1, 0, 7]
    for num1, num2 in zip(numbers):
        if math.abs(num1 - num2) <= threshold:
            return True
    return False

# Test the function
numbers = [1.0, 2.0, 3.0, 4, 5, 6, 7, 8, 9, 0, 0.0, 9, 10]
print(has_close_elements(numbers, 0.0))
print(has_close_elements([1.0, 2.0, 3.0, 4], 5, 6, 7, 8, 9, 0, 0], 10))
```
This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input. The function loops through all the numbers in the list and checks if the absolute value of any number in the list is less than or equal to the threshold. The function returns True if any two numbers are closer to each other than the threshold, otherwise, it returns False.