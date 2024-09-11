```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of floats with a length of at least 2.

    Returns:
    A tuple of two floats representing the closest elements in the input list, in ascending order.
    """
    
    # Check if the input list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements")

    # Initialize minimum difference and the pair of closest numbers with the first two elements in the list
    min_diff = abs(numbers[1] - numbers[0])
    closest_pair = (numbers[0], numbers[1])

    # Iterate over the list of numbers to find the closest pair
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[j] - numbers[i])
            # Update the minimum difference and the closest pair if a closer pair is found
            if diff < min_diff:
                min_diff = diff
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

However, this solution has a time complexity of O(n^2) due to the nested loops. For large lists, a more efficient solution would be to sort the list first, then iterate over it once to find the closest pair, resulting in a time complexity of O(n log n) due to the sorting:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of floats with a length of at least 2.

    Returns:
    A tuple of two floats representing the closest elements in the input list, in ascending order.
    """
    
    # Check if the input list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize minimum difference and the pair of closest numbers with the first two elements in the list
    min_diff = numbers[1] - numbers[0]
    closest_pair = (numbers[0], numbers[1])

    # Iterate over the sorted list of numbers to find the closest pair
    for i in range(1, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        # Update the minimum difference and the closest pair if a closer pair is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
