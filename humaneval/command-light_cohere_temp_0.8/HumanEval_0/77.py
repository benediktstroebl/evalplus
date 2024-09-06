```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False
```
This script defines a function that checks if any two consecutive elements in a given list are closer to each other than a given threshold. 

The function iterates through the list elements, and checks if the difference between consecutive elements is less than the given threshold. If it is true, the function returns True, indicating that there are close elements in the list.

You can use this function with your problem as intended, and the function will return True if the problem is satisfied.