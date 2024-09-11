```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        Tuple[float, float]: A tuple of two float numbers that are the closest to each other

    Raises:
        ValueError: If the list of numbers has less than two elements
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list of numbers must have at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first two elements

    # Iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the two numbers that are the closest to each other. The function first checks if the list has at least two elements. If not, it raises a `ValueError`. Then, it sorts the list of numbers and initializes the minimum difference and the closest pair. It iterates over the list to find the closest pair by calculating the difference between each pair of adjacent numbers and updating the minimum difference and the closest pair if a smaller difference is found. Finally, it returns the closest pair. The script includes test cases to demonstrate the function's behavior.