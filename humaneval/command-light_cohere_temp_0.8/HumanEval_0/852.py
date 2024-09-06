```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Sort the list of numbers
    numbers.sort(key=lambda x: (x, -x))
    # Iterate over list elements and compare adjacent elements
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] - numbers[i] < threshold:
                return True
    return False

# Test the function
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 8.0]
return has_close_elements(numbers, 0.0)  # False  # No two elements are closer than 0.0
```
This function, `has_close_elements`, checks if in a list of numbers, any two elements are closer to each other than a given threshold. The function uses the sorting algorithm, specifically, a sorting key function that compares two adjacent elements, to determine if any two elements are closer to each other than the threshold.