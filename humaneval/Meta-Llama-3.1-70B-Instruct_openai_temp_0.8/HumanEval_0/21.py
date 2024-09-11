```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate through the sorted list with the index and value
    for i, num in enumerate(numbers):
        # We start checking from the next number
        for next_num in numbers[i+1:]:
            # If the difference between the current number and the next number is less than the threshold, return True
            if next_num - num < threshold:
                return True
            # If the difference is greater than or equal to the threshold, we can break the loop because the list is sorted
            else:
                break

    # If we've checked all numbers and haven't returned True, it means no two numbers are closer than the threshold
    return False


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
    print(has_close_elements([1.0, 1.01, 1.02, 1.03], 0.01))  # True
    print(has_close_elements([1.0, 10.0, 100.0], 5.0))  # False
```