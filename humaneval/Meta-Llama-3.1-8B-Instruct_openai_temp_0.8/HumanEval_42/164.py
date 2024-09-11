```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.
    
    Args:
        l (list): The list to increment.
    
    Returns:
        list: The incremented list.
    """
    return [x + 1 for x in l]


# Test cases
import unittest

class Testincr_list(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_multiple_types(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```

In this script, we define a function `incr_list` that takes a list `l` as input, and returns a new list where each element is incremented by 1. This function uses a list comprehension to create the new list.

The test cases use the `unittest` module to ensure that the function behaves as expected. We define two test cases: `test_base_case` tests the function with the base case of `[1, 2, 3]`, and `test_multiple_types` tests the function with a list that contains different types of numbers. If all test cases pass, the function is working correctly.