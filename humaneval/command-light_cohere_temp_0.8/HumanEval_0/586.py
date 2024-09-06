Here is a self-contained Python function that solves the problem you have described:
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

# Test case
has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.3)


Output:
True

This function loops over the list of numbers and checks if any two consecutive elements are closer than the given threshold.