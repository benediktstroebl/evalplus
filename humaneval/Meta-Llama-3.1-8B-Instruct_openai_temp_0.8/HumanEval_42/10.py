```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: The input list with each element incremented by 1.
    """
    return [x + 1 for x in l]


# Test cases
import unittest

class TestIncrList(unittest.TestCase):
    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == "__main__":
    unittest.main()
```

In this script, we define the `incr_list` function which uses a list comprehension to increment each element in the input list by 1. We then use the `unittest` framework to test this function with the provided test cases. If the function is working correctly, it will pass the tests.