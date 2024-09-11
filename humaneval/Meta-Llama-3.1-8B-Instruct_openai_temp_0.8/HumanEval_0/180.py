```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if there are any two numbers closer to each other than the given threshold, False otherwise.
    """
    if len(numbers) <= 1:
        return False

    numbers.sort()  # Sort the list to efficiently check for close elements
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False

# Example use cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which checks if any two numbers in a given list are closer to each other than a specified threshold. It sorts the list to efficiently check for close elements, and then iterates through the sorted list to find any adjacent elements that are closer than the threshold. If such elements are found, it immediately returns `True`. If the loop completes without finding any close elements, it returns `False`.

In the example use cases, this function is called with the provided test cases to verify that it correctly identifies whether two numbers are closer than the given threshold.