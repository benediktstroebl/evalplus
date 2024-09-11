### Find Closest Elements in a List
#### Problem Description
From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers of length at least two.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    numbers.sort()
    closest_diff = float('inf')
    closest_pair = ()

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < closest_diff:
            closest_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
```
#### Explanation
This script uses a simple sorting approach to find the two closest numbers in the list. The `sort` method is used to sort the list in ascending order. Then, it iterates through the sorted list, keeping track of the pair of numbers with the smallest difference. The pair with the smallest difference is returned as the result.

#### Example Use Cases
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```