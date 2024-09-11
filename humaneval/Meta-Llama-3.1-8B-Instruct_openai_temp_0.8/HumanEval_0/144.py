```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to consider them close.

    Returns:
        bool: True if there are any two numbers closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between current number and next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If it is, return True immediately
            return True
    
    # If we have checked all numbers and haven't found any close elements, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("Test case 1 failed: [1.0, 2.0, 3.0], 0.5 should return False")
else:
    print("Test case 1 passed")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("Test case 2 failed: [1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3 should return True")
else:
    print("Test case 2 passed")
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns True if there are any two numbers closer than the threshold, and False otherwise. The function sorts the list of numbers in ascending order, then iterates over the sorted list to check for close elements. If it finds any close elements, it returns True immediately. If it checks all numbers and doesn't find any close elements, it returns False. The script also includes two test cases to verify the correctness of the function.