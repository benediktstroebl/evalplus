```markdown
## Closest Elements in a List
### Problem Description
Find two numbers in a given list that are the closest to each other and return them in order (smaller number, larger number).

### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # First, sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = None
    
    # Iterate through the sorted list to find the closest pair of numbers
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair
```
### Example Use Cases
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# Output: (2.0, 2.2)

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
# Output: (2.0, 2.0)
```
This script uses the built-in Python `sorted` function to sort the input list in ascending order. It then iterates through the sorted list to find the closest pair of numbers by keeping track of the minimum difference found so far. The closest pair of numbers is returned as a tuple.