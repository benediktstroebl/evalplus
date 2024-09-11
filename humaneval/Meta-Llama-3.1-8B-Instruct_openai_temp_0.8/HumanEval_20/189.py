```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are the closest to each other.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    numbers.sort()
    min_diff = float('inf')  # Initialize minimum difference as infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize closest pair as the first two numbers

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between current and next numbers
        if diff < min_diff:
            min_diff = diff  # Update minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update closest pair

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script first checks if the list has at least two elements. If not, it raises a `ValueError`. Then it sorts the list and initializes `min_diff` as infinity and `closest_pair` as the first two numbers. It then iterates over the sorted list and checks the difference between current and next numbers. If the difference is less than `min_diff`, it updates `min_diff` and `closest_pair`. Finally, it returns `closest_pair`.