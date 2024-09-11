### Closest Elements Finder
```markdown
Find the two closest elements in a list of numbers.
### Usage
```python
from closest_elements import find_closest_elements

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
smallest, largest = find_closest_elements(numbers)
print(f"Smallest: {smallest}, Largest: {largest}")
```

### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: The two closest numbers in order.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[0])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = sorted_numbers[i + 1] - sorted_numbers[i]

        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair
```

### Explanation
This script defines a function `find_closest_elements` that takes a list of numbers as input and returns the two closest numbers in the list. The function sorts the list of numbers and then iterates over the sorted list to find the pair of numbers with the smallest difference. The closest pair is returned as a tuple. If there are multiple pairs with the same smallest difference, the function returns the first pair it encounters.