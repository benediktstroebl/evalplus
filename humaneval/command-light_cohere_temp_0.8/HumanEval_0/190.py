Here is a self-contained Python script that defines a function called `has_close_elements` which checks if any two elements in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)-1):
        if numbers[i] - numbers[i-1] < threshold:
            return True
    return False
```
This code evaluates if any two elements in the list are closer than the given threshold. The list can contain any floating-point numbers and the function returns `True` if the condition is met, indicating that two elements are close. 
The function works by comparing each pair of elements in the list, starting from the second element. The first element is compared to the previous element, and `threshold` is the minimum distance between any two elements.