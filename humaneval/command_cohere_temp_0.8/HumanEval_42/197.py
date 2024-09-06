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
    def test_incr_list(self):
        # Regular case
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

        # Edge cases
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        self.assertEqual(incr_list([0, 0, 0, 5, 6, 7, 8, 9]), [1, 1, 1, 6, 7, 8, 9, 10])

        # Single element
        self.assertEqual(incr_list([4]), [5])

        # Empty list
        self.assertEqual(incr_list([]), [])

    def test_incr_list_with_negative_elements(self):
        # Regression test for #1
        self.assertEqual(incr_list([-1, -2, -3]), [0, -1, -2])

if __name__ == '__main__':
    unittest.main()
```
This test suite contains two test cases: `test_incr_list` and `test_incr_list_with_negative_elements`. The first test case verifies the function's behavior on a regular list, while the second one checks if the function correctly handles negative elements. 

To run the tests, simply execute the script. The `unittest` framework will run each test method, and at the end it will report on the number of tests passed or failed. 

This example demonstrates how to write testable code and verify the expected behavior of a function using `unittest`. 

I hope this solution and additional testing approach meet your requirements. Let me know if you have any other questions or if you'd like to further refine the testing approach!