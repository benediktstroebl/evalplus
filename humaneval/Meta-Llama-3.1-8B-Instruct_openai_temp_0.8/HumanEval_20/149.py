Here is a Python script that uses the built-in `sorted` function and a custom key function to solve the problem:

```markdown
### Closest Elements Finder

This script finds the two numbers in a list that are closest to each other.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # First, we sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Then, we initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # We iterate over the sorted list to find the pair with the minimum difference
    for i in range(1, len(sorted_numbers)):
        # Calculate the difference between the current number and the previous one
        diff = sorted_numbers[i] - sorted_numbers[i-1]
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i-1], sorted_numbers[i])
    
    # Finally, we return the pair of closest numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script works by first sorting the list of numbers in ascending order. Then, it iterates over the sorted list to find the pair of numbers with the minimum difference. The minimum difference and the closest pair are updated whenever a smaller difference is found. Finally, the script returns the pair of closest numbers.

This solution has a time complexity of O(n log n) due to the sorting step, where n is the length of the input list. The subsequent iteration over the sorted list has a time complexity of O(n), but it does not dominate the time complexity of the sorting step in terms of big-O notation.

It's worth noting that this solution assumes that the input list contains at least two elements. If the input list can be empty or contain only one element, additional error handling may be necessary.