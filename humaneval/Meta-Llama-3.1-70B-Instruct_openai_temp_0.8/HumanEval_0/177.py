```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """

    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with a for loop and an enumerate
    # to get both the index and the value of each element.
    for i, num in enumerate(numbers):
        
        # We skip the first element because we're comparing each element with its next one.
        if i == 0:
            continue
        
        # For each element, we calculate the difference with its previous one.
        difference = num - numbers[i - 1]
        
        # If the difference is less than or equal to the threshold, we return True.
        if difference <= threshold:
            return True
    
    # If we've iterated over the entire list without finding any close elements, we return False.
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```