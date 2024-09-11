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
    numbers.sort()  # Sort the list to bring close numbers together
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if numbers[i + 1] - numbers[i] < threshold:  # Check if the difference is less than the threshold
            return True  # If it is, return True
    return False  # If no close numbers are found, return False


# Test cases
if __name__ == "__main__":
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    assert has_close_elements([1.0, 1.1], 1.0)
    assert not has_close_elements([1.0, 1.1], 0.01)
    print("All test cases pass")
```