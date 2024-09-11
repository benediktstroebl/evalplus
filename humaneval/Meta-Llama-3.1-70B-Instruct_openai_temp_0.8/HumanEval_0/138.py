```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list with the index and value
    for i, num in enumerate(numbers):
        # We start checking from the next number
        for next_num in numbers[i + 1:]:
            # If the difference between the current number and the next number is less than or equal to the threshold
            if next_num - num <= threshold:
                # We return True, indicating that two numbers are closer than the threshold
                return True
    
    # If we have checked all numbers and haven't found any that are closer than the threshold, we return False
    return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

However, the above solution has a time complexity of O(n^2) due to the nested loop. Here is a more efficient solution with a time complexity of O(n log n) due to the sorting:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we iterate over the sorted list with the index and value
    for i in range(len(numbers) - 1):
        # If the difference between the current number and the next number is less than or equal to the threshold
        if numbers[i + 1] - numbers[i] <= threshold:
            # We return True, indicating that two numbers are closer than the threshold
            return True
    
    # If we have checked all numbers and haven't found any that are closer than the threshold, we return False
    return False


# Example use cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```