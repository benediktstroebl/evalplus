### Closest Elements Finder

Below is a Python script that uses the built-in `sorted` function and a custom key function to find the two closest elements in a list.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two closest elements in a list of numbers.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple of two closest numbers in the list.

    Raises:
    ValueError: If the list contains less than two elements.
    """
    
    # Check if the list contains less than two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Sort the list
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
# (2.0, 2.0)
```

This script uses the `sorted` function to sort the input list. Then it iterates over the sorted list to find the pair of elements with the minimum difference. The pair is returned as a tuple. If the list contains less than two elements, a `ValueError` is raised.