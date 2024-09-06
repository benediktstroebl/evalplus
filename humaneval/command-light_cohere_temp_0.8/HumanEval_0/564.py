Here is a self-contained Python function that solves the problem of determining if any two numbers in a list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] <= threshold:
            return True
    return False
```
The function takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold.

The function first sorts the numbers list in ascending order. Then, it loops over the range of the list, checking if the difference between the current number and the next number is less than or equal to the threshold. If this condition is met, the function returns True, indicating that there are closer numbers in the list.