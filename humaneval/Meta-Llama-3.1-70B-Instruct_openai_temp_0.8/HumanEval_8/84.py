```python
from typing import List, Tuple
import unittest
import math


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and product of the integers in the list.
    """
    total_sum = sum(numbers)
    total_product = math.prod(numbers) if numbers else 1
    return total_sum, total_product


class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_element_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_zero(self):
        self.assertEqual(sum_product([1, 2, 0, 4]), (7, 0))

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, -24))


if __name__ == '__main__':
    unittest.main()
```