```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return True if any two distinct elements in the list are closer than threshold, False otherwise
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test the function with an example input
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
return has_close_elements(numbers, 0.0.5)
``` Output should be True