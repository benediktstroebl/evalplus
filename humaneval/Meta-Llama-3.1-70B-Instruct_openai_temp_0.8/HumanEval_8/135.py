```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Tuple[int, int]: A tuple containing the sum and the product of the input list.
    """
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1

    # Iterate over the list to calculate sum and product
    for num in numbers:
        total_sum += num
        total_product *= num

    # Return the calculated sum and product
    return total_sum, total_product


# Test cases
import unittest

class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_zeros(self):
        self.assertEqual(sum_product([1, 0, 2, 0, 3]), (6, 0))

if __name__ == '__main__':
    unittest.main()
```