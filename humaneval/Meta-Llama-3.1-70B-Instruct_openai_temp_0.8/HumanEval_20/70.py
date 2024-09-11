```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: Two numbers in the list that are closest to each other, in order.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")

    numbers.sort()  # sort the list in ascending order

    min_diff = float('inf')  # initialize the minimum difference as infinity
    closest_pair = ()  # initialize the closest pair as an empty tuple

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # calculate the difference between two adjacent numbers
        if diff < min_diff:  # if the difference is smaller than the current minimum difference
            min_diff = diff  # update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # update the closest pair

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```