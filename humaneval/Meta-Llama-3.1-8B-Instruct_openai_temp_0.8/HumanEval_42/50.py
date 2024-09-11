### Increment List Elements
#### Code

```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of numbers to increment.

    Returns:
        list: List with elements incremented by 1.
    """
    return [i + 1 for i in l]

# Test cases
if __name__ == "__main__":
    import unittest

    class TestIncrList(unittest.TestCase):
        def test_increment_numbers(self):
            self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        def test_increment_mixed_numbers(self):
            self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    unittest.main(argv=[sys.argv[0]])

```
#### Explanation
This script uses a list comprehension to increment each element in the input list `l` by 1. The `unittest` module is used to write and run test cases for the `incr_list` function.

The test cases cover two different scenarios: incrementing a list of consecutive numbers, and incrementing a list of mixed numbers. If the test cases pass, it gives confidence that the `incr_list` function is working correctly.

#### Running the Script
To run the script, save it to a file (e.g. `incr_list.py`) and execute it using Python:

```bash
python incr_list.py
```