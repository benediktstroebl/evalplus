```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers to make it easier to check for close elements
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list of numbers
    for i in range(len(sorted_numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            # If a close pair is found, return True immediately
            return True

    # If no close pairs are found after checking the entire list, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print("False")
else:
    print("has_close_elements([1.0, 2.0, 3.0], 0.5) should return False")

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print("True")
else:
    print("has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) should return True")
```

However, this solution has a time complexity of O(n^2) because it checks each pair of numbers in the list. We can improve this to O(n log n) by using the fact that the numbers are sorted:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Iterate over the sorted list of numbers
    for i in range(len(sorted_numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            # If a close pair is found, return True immediately
            return True

    # If the list is sorted, we can use binary search to check if any two numbers are close
    for num in sorted_numbers:
        # Find the closest number to the current number in the sorted list
        closest_num = find_closest_num(sorted_numbers, num)

        # Check if the difference between the current number and its closest number is less than the threshold
        if num - closest_num < threshold:
            # If a close pair is found, return True immediately
            return True

    # If no close pairs are found after checking the entire list, return False
    return False

def find_closest_num(numbers: List[float], target: float) -> float:
    """
