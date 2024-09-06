Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To confirm the function's behavior, let's test it using Python's built-in `unittest` framework:
```python
import unittest

class TestIncList(unittest.TestCase):
    def test_incr_list_with_regular_list(self):
        # Regular List
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_incr_list_with_list_with_duplicates(self):
        # List with Duplicates
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()
```
This above code passes two test cases to ensure the function `incr_list` behaves as expected. The first test case sends a regular list, while the second test case sends a list with duplicates, ensuring that the function correctly increments both kinds of input.  The `unittest` framework runs these tests and verifies that they pass, giving us confidence that our function works as expected.  In the incorporated style, this code will run the tests automatically when the script is executed directly.