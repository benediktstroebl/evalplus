Here's a self-contained Python function that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any( abs(num1 - num2) <= threshold for num1, num2 in zip(numbers))
```
This function utilizes the absolute difference between any two numbers in the list to check if the difference is less than the specified threshold.