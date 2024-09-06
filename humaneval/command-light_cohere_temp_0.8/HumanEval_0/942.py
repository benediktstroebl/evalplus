Here is a Python script that solves the problem you provided:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
   
    numbers = sorted(numbers)  # Sort the list to ensure elements were in increasing order
    # Sorting in ascending order
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] - numbers[i] <= threshold:
                return True
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Thiss pass on
```