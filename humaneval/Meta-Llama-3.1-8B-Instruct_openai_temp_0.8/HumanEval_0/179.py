```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The minimum distance between two numbers to be considered as close.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the distance between the current number and the next number
        distance = numbers[i + 1] - numbers[i]

        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True

    # If no pair of numbers is closer than the threshold, return False
    return False


# Example usage:
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

In this script, the `has_close_elements` function takes a list of numbers and a threshold as input, sorts the list, and then iterates over the sorted list to check if any two numbers are closer than the threshold. If such a pair is found, the function immediately returns `True`. If no such pair is found after checking all numbers, the function returns `False`. The example usage section demonstrates how to use the function with the provided test cases.