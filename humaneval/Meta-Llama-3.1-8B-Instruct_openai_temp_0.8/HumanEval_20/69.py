### Find Closest Elements
#### Problem Description
Find two numbers in a list that are the closest to each other and return them in order.

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each 
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of float numbers.

    Returns:
        A tuple of two float numbers that are the closest to each other in order.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])

    # Return the closest pair of numbers
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

#### Explanation
The function `find_closest_elements` takes a list of float numbers as input, sorts them in ascending order, and then iterates over the sorted list to find the closest pair of numbers. It keeps track of the minimum difference between two consecutive numbers and the corresponding pair of numbers. Finally, it returns the closest pair of numbers. The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input list.