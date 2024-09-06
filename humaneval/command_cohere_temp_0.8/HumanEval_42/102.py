Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

To confirm the function's behavior, let's test it using Python's built-in `unittest` module:
```python
import unittest

class TestIncList(unittest.TestCase):
    def test_incr_list(self):
        # Regular case
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        # Edge cases
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        # Empty list case
        self.assertEqual(incr_list([]), [])
        
    def test_incr_list_with_negative_elements(self):
        # Test with negative elements and verify correctness
        self.assertEqual(incr_list([-1, -2, -3]), [-2, -1, -4])
        
if __name__ == '__main__':
    unittest.main()
```
This test suite includes two test cases: `test_incr_list` verifies the functionality with both a regular list and an edge case list, and `test_incr_list_with_negative_elements` verifies the functionality with a list containing negative integers. 

To run the tests, simply execute the script. The `unittest` framework will run each test case, and if all tests pass, it will print `OK` indicating a successful test run. If any test fails, `unittest` will provide details about the failure. 

This example demonstrates how to define a function, write test cases, and utilize a testing framework to verify the function's behavior, ensuring the function works correctly across various scenarios.