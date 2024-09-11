```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the closest numbers
    min_diff = float('inf')
    closest_nums = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the closest numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i + 1])
    
    return closest_nums

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script first sorts the list of numbers and then iterates over the sorted list to find the closest numbers. It keeps track of the minimum difference and the closest numbers found so far. The time complexity of this script is O(n log n) due to the sorting operation, where n is the length of the list. The space complexity is O(1) if the input list is not considered as extra space, otherwise it's O(n) for the sorting operation.