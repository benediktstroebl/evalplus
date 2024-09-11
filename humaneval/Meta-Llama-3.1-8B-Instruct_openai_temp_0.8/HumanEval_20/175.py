### Find Closest Pairs of Numbers
#### Problem Statement
Given a list of numbers, find the two numbers that are closest to each other and return them in order.

#### Solution
```markdown
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
    and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')  # Initialize with infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first two numbers

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair of numbers
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

#### Explanation
This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers. The function first sorts the list of numbers in ascending order. Then, it iterates over the sorted list to find the closest pair of numbers by keeping track of the minimum difference and updating the closest pair whenever a smaller difference is found. Finally, the function returns the closest pair of numbers.