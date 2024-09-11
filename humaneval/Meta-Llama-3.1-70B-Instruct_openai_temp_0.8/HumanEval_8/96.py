```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple of two integers. The first integer is the sum of all integers in the list and the second integer is the product of all integers in the list.
    """
    # Initialize sum and product with default values for empty list
    total_sum = 0
    total_product = 1
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add the current number to the total sum
        total_sum += num
        
        # Multiply the current number with the total product
        total_product *= num
    
    # Return the total sum and total product as a tuple
    return total_sum, total_product


# Test cases
import unittest

class TestSumProductFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_list_with_zero(self):
        self.assertEqual(sum_product([0, 1, 2, 3]), (6, 0))

if __name__ == '__main__':
    unittest.main()
```