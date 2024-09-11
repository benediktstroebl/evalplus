### Find Closest Elements in a List
#### Problem Description
From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds two numbers in the list that are the closest to each other.

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple containing two numbers that are the closest to each other.

    Raises:
        ValueError: If the list contains less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # First, sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the pair of closest numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
```

#### Example Use Cases
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```
Note that this solution has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input list. If the list is already sorted or if the numbers are close to each other, a more efficient solution with a time complexity of O(n) can be implemented using a two-pointer technique.