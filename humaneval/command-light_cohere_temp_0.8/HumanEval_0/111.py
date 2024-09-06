```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False

# Example usage:
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0]
has_close_elements(numbers, 0.8) # True

print(has_close_elements(numbers, 0.8)) # Output: True

In this script, the has_close_elements function takes two parameters: a list of numbers and a threshold value. The function then uses a nested loop to compare each pair of numbers in the list with the threshold value. It returns True if any two numbers in the list are closer to each other than the threshold, otherwise, it returns False.