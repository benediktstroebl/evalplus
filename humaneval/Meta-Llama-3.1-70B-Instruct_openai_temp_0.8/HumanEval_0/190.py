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
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with index and value
    for i in range(len(numbers) - 1):
        # For each number, we calculate the difference with the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than or equal to the threshold, we return True
        if difference <= threshold:
            return True

    # If we have checked all numbers and haven't found any pair closer than the threshold, we return False
    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```