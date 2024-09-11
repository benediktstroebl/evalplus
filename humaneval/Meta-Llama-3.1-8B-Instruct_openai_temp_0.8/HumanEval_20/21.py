Here's a Python script that solves the problem in a self-contained way using the built-in `sorted` function and list slicing.
```markdown
### Solution: Closest Elements in a List

#### Problem
From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

#### Code
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating point numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[0])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = sorted_numbers[i + 1] - sorted_numbers[i]

        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(numbers))  # Output: (2.0, 2.2)
```

#### Alternative Solution Using Built-in `sorted` Function and List Slicing

Here's a more concise solution that uses the built-in `sorted` function and list slicing to find the closest pair of numbers.
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating point numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Sort the list of numbers
    sorted