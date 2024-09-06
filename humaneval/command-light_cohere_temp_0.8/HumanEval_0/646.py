Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] <= threshold:
            return True
    return False
```

This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input. The function loops through the each element in the list, except the last one, and checks if the current element is within the threshold of the next element. If any condition is met, the function returns True, indicating that there are elements in the list that are close to each other.