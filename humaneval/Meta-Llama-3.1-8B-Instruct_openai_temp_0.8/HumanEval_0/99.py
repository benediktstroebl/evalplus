### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to check each pair of adjacent numbers
    for i in range(1, len(sorted_numbers)):
        # Calculate the distance between the current number and the previous one
        distance = sorted_numbers[i] - sorted_numbers[i - 1]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True
    
    # If no pair of numbers is closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation
This solution sorts the list of numbers and then iterates over the sorted list to check each pair of adjacent numbers. For each pair, it calculates the distance between the current number and the previous one. If the distance is less than the threshold, it returns True immediately. If no pair of numbers is closer than the threshold, it returns False at the end. The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input list. The space complexity is O(n) for the sorted list.