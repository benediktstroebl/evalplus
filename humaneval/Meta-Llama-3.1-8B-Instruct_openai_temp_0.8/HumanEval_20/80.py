Here is a Python script that solves the problem using a brute-force approach:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers of length at least two.

    Returns:
    Tuple[float, float]: A tuple containing the two numbers that are the closest to each other.
    """

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over all pairs of numbers in the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            diff = abs(numbers[i] - numbers[j])

            # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    # Return the closest pair of numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script has a time complexity of O(n^2) due to the nested loops, where n is the number of elements in the input list. For large lists, this may be slow. If you need a more efficient solution, you could use a sorting-based approach, which would have a time complexity of O(n log n).