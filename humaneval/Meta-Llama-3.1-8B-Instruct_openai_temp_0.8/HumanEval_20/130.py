### Find Closest Elements in a List of Numbers
#### Python Script
```markdown
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple containing two numbers that are the closest to each other in the input list.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest pair of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

#### Explanation

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple containing the two numbers that are closest to each other in the list.

The function first checks if the input list has at least two elements. If not, it raises a `ValueError`.

Next, the function sorts the list in ascending order using the `sort` method.

Then, it iterates over the sorted list to find the closest pair of numbers. It keeps track of the minimum difference between adjacent numbers and the corresponding pair of numbers.

Finally, the function returns the closest pair of numbers as a tuple.

The script includes two test cases to demonstrate the function's behavior.