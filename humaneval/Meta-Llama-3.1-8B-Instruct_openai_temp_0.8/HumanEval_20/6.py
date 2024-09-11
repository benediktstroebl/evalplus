### Closest Elements Finder
#### Problem Statement
Find two numbers in a list that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
    and return them in order (smaller number, larger number).

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
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the pair of closest numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This script defines a function `find_closest_elements` that takes a list of floating point numbers and returns a tuple containing the two closest numbers in the list. The function first sorts the list in ascending order, then iterates over the sorted list to find the pair of closest numbers. The function keeps track of the minimum difference between consecutive numbers and updates the closest pair whenever a smaller difference is found. The script also includes two test cases to demonstrate the function's behavior.