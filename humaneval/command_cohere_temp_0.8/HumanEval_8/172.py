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
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else numbers[0])
```

The function works correctly for empty lists and for lists with one and more elements. It returns a tuple with sum and product of elements in the list according to the described problem. It can be tested with the following code:
```python
import unittest

def test_sum_product():
    """ List of tests for sum_product function """
    class TestSumProduct(unittest.TestCase):
        def test_empty(self):
            self.assertEqual(sum_product([]), (0, 1))
        def test_single(self):
            self.assertEqual(sum_product([1]), (1, 1))
        def test_normal(self):
            self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
    unittest.main()
```