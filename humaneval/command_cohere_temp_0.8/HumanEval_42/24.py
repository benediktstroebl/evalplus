Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To confirm the function's behavior, let's test it using Python's built-in `unittest` module:
```python
import unittest

class TestIncList(unittest.TestCase):
    def test_incr_list(self):
        # Regular case
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

        # Edge cases
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        self.assertEqual(incr_list([0, 0, 0, 5, 6, 7, 8, 9, 10]), [1, 1, 1, 6, 7, 8, 9, 10, 11])

    def test_incr_list_empty(self):
        self.assertEqual(incr_list([]), [])

if __name__ == '__main__':
    unittest.main()
```
We have used `unittest` framework to carry out our tests. In this case, we've created a test class `TestIncList` that inherits from `unittest.TestCase`. This class contains two test methods, `test_incr_list` and `test_incr_list_empty`, which exercise distinct scenarios of the `incr_list` function. Finally, `unittest.main()` is called to discover and run the test cases. 

Running this script will execute the tests and display a passing indicator for each test case if the function's behavior matches the expected output.