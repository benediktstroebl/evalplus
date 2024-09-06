```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If the number is less than the threshold, then it is treated as close
    The closer, the larger the number.
    """
    # checking if two elements are closer than the threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# Test the function
# [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3] # True
```

Output: True

The function has_close_elements takes a List[float] numbers and a float threshold as input and returns a bool indicating whether any two elements in the list are closer than the threshold. The function uses a Two-pointer technique to iterate over the list and checks if any two elements are closer than the threshold.