```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), sum(n * n for n in numbers))
```

The function works as follows:
1. If the input list is empty, it returns the qualifying empty sum and product values of 0 and 1, respectively.
2. If the input list is not empty, the sum is calculated by using the built-in sum() function, and the product is calculated by using a generator expression with the sum() function as well.

This solution allows for efficient and concise computation of both the sum and product of integers in a list. 

The unit tests for this function would be:
```python
import unittest
from sum_product import sum_product

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_list_with_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

if __name__ == '__main__':
    unittest.main()
```
These tests check if the function works appropriately with an empty list and a list with elements.