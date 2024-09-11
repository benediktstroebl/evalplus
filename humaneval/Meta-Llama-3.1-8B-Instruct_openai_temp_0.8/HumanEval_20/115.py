### Find Closest Elements in a List
#### A Python Script
```markdown
### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) 
    select and return two that are the closest to each other 
    and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of at least two numbers.

    Returns:
    Tuple[float, float]: The two closest numbers.

    Example:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the closest pair
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i-1], numbers[i])

    return closest_pair

### Example Usage
if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
#### Explanation

This script defines a function `find_closest_elements` that takes a list of numbers as input. It first checks if the list has at least two elements. If not, it raises a `ValueError`. Otherwise, it sorts the list and initializes the minimum difference and the closest pair. It then iterates over the list to find the closest pair by checking the difference between each pair of adjacent numbers. If a smaller difference is found, it updates the minimum difference and the closest pair. Finally, it returns the closest pair.

The example usage demonstrates how to call the function with different input lists and print the results.