```python
from typing import List, Tuple
from math import prod
import unittest


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    Args:
    numbers (List[int]): A list of integers.
    
    Returns:
    Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    # Calculate the sum of the list using built-in sum function
    total_sum = sum(numbers)
    
    # Calculate the product of the list using math.prod function
    # math.prod returns 1 for an empty list, which is in line with the problem requirements
    total_product = prod(numbers)
    
    return total_sum, total_product


class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_product([-1, 2, -3, 4]), (2, -12))

    def test_list_with_zeros(self):
        self.assertEqual(sum_product([0, 1, 0, 2]), (3, 0))


if __name__ == '__main__':
    unittest.main()
```

This script defines a function `sum_product` that calculates the sum and product of a given list of integers. The function is tested with a set of unit tests to ensure its correctness. The `math.prod` function is used to calculate the product of the list, as it naturally returns 1 for an empty list, which aligns with the problem requirements.