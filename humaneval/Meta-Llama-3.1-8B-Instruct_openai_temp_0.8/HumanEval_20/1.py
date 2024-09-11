### Find Closest Elements in a List
#### Script
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of float numbers with at least two elements.

    Returns:
    A Tuple of two float numbers that are the closest to each other.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current pair
        diff = numbers[i + 1] - numbers[i]

        # Update the minimum difference and the closest pair if needed
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
import unittest

class TestFindClosestElements(unittest.TestCase):

    def test_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_list_with_single_element(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

    def test_list_with_two_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))

if __name__ == '__main__':
    unittest.main()
```
#### Explanation

This script defines a function `find_closest_elements` that takes a list of float numbers as input and returns a tuple of two float numbers that are the closest to each other. The function first checks if the list has at least two elements. If not, it raises a `ValueError`.

Then, it sorts the list in ascending order and iterates over the sorted list to find the closest pair. It keeps track of the minimum difference and the closest pair.

The script also includes test cases to ensure the function works correctly. The test cases cover different scenarios, including lists with different lengths and edge cases.

#### Usage

To use this script, simply run it in your Python environment. The script will run the test cases and report any errors. You can also call the `find_closest_elements` function with a list of float numbers as input to find the closest pair.