```python
from typing import List, Tuple
import heapq

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    Tuple[float, float]: A tuple of two float numbers that are the closest to each other.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Use a heap to find the closest pair
    heap = []
    for i in range(len(numbers) - 1):
        heapq.heappush(heap, (numbers[i + 1] - numbers[i], numbers[i], numbers[i + 1]))

    # The heap will contain the differences between adjacent numbers in the sorted list.
    # We pop the smallest difference from the heap and return the corresponding adjacent numbers.
    # If the smallest difference is between the same number, return that number twice.
    min_diff, _, closest_pair = heapq.heappop(heap)
    while heap and (closest_pair[0] == closest_pair[1] or (heap[0][0] == min_diff and heap[0][1] == closest_pair[0])):
        min_diff, _, closest_pair = heapq.heappop(heap)

    return closest_pair

# Test cases
import unittest
class TestFindClosestElements(unittest.TestCase):
    def test_closest_elements(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

if __name__ == '__main__':
    unittest.main()
```

The `find_closest_elements` function takes a list of numbers and returns a tuple of two numbers that are the closest to each other. It uses a heap to find the closest pair. If the smallest difference is between the same number, it returns that number twice. The function also checks if the list has at least two elements.