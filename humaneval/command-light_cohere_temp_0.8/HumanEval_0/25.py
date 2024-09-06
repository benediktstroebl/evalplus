```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    : Return True if any two distinct numbers in the list are less than the threshold, otherwise False
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test
# pass has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 8])

# 6.

True