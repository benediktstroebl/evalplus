```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    Tuple[float, float]: A tuple containing two numbers that are the closest to each other.
    """
    
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between the current and next numbers
        if diff < min_diff:  # If the difference is smaller than the current minimum difference
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update the pair of closest numbers
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

In this script, the `find_closest_elements` function takes a list of numbers as input, sorts the list in ascending order, and then iterates over the sorted list to find the pair of numbers with the minimum difference. The function returns this pair of numbers as a tuple.

The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input list. The space complexity is O(n) for the sorting step.