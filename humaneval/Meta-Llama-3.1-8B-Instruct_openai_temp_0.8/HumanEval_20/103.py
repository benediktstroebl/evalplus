```markdown
### Find Closest Elements in a List

This Python script finds two numbers in a list that are the closest to each other.

#### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: The two closest numbers in the list.

    Example:
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
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest numbers
        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i + 1])

    return closest_nums

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

#### Explanation

This script first sorts the list of numbers in ascending order. Then, it iterates over the sorted list to find the closest numbers. It keeps track of the minimum difference between two consecutive numbers and the corresponding closest numbers. Finally, it returns the closest numbers.

The time complexity of this script is O(n log n) due to the sorting step, where n is the number of elements in the list. The space complexity is O(n) for the sorted list.