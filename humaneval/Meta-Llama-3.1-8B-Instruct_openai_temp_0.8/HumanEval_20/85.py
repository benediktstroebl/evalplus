```markdown
### Closest Pair of Numbers in a List

This Python script finds the two numbers in a list that are closest to each other.

#### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        Tuple[float, float]: A tuple of two floating-point numbers that are the closest to each other.

    Example:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Check if the input list is empty or contains less than two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the pair of closest numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next number
        diff = abs(numbers[i] - numbers[i + 1])

        # Update the minimum difference and the pair of closest numbers if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

#### Explanation

1.  The script starts by importing the necessary `List` and `Tuple` types from the `typing` module for type hinting.
2.  The `find_closest_elements` function takes a list of floating-point numbers as input and returns a tuple of two numbers that are the closest to each other.
3.  It first checks if the input list is empty or contains less than two elements and raises a `ValueError` in such cases.
4.  The list is then sorted in ascending order using the `sort` method.
5.  The script initializes the minimum difference (`min_diff`) to infinity and the pair of closest numbers (`closest_pair`) to the first element of the list.
6.  It iterates over the sorted list, calculating the absolute difference between each pair of consecutive numbers.
7.  If a smaller difference is found, it updates the minimum difference and the pair of closest numbers.
8.  Finally, it returns the pair of closest numbers.

You can run this script to test the `find_closest_elements` function with different input lists.