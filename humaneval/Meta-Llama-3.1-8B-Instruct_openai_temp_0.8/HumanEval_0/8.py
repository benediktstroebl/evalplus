```markdown
### Solution: has_close_elements Function

#### Problem Description
Check if in given list of numbers, are any two numbers closer to each other than given threshold.

#### Solution
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
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        # Check if the difference between current and next element is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If close elements are found, return True
            return True

    # If no close elements are found after iterating over the entire list, return False
    return False

### Example Usage
if __name__ == "__main__":
    # Test case 1: No close elements
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False

    # Test case 2: Close elements found
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

### Notes
This solution works by first sorting the list of numbers in ascending order. Then, it iterates over the sorted list to check for pairs of elements that are closer than the given threshold. If such a pair is found, the function immediately returns `True`. If the function finishes iterating over the list without finding any close elements, it returns `False`. The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n) for the sorted list.