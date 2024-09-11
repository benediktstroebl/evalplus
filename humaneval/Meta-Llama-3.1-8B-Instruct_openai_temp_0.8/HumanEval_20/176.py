```markdown
### Python Script to Find Closest Elements in a List
```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in the list.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Use itertools.groupby to group the numbers by their distances
    grouped_numbers = itertools.groupby(sorted_numbers, key=lambda x: abs(x - sorted_numbers[0]))

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the groups
    for key, group in grouped_numbers:
        # Convert the group to a list and sort it
        group_list = sorted(list(group))

        # If the group contains more than one element, update the minimum difference and the closest pair
        if len(group_list) > 1:
            diff = group_list[1] - group_list[0]
            if diff < min_diff:
                min_diff = diff
                closest_pair = (group_list[0], group_list[1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script uses the `itertools.groupby` function to group the numbers by their distances. It then iterates over the groups and updates the minimum difference and the closest pair of numbers. The function returns the closest pair of numbers in the list.