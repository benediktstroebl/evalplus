```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Sort the in ascending order
    numbers = sorted(numbers)

    # loop in reverse order
    for i in range(len(numbers)-1):
        if numbers[i] - numbers[i+1] <= threshold:
            return True

    return False
```
The above function will check each pair of adjacent elements in numbers and check if the difference between the two numbers is less than or equal to the threshold. It will return True if there is any such pair that meets this condition.