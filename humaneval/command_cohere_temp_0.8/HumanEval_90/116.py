```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mx, mn = max(lst), min(lst)
    return mx if mx == mn else mn + 1
```
The function `next_smallest()` employs list comprehension and the `max()` and `min()` functions to find the maximum and minimum values in the list. It then returns the maximum value if it is the second-smallest value or the minimum value plus 1 if the maximum and minimum differ. 

Here is how you could test this function using Python's built-in `unittest` framework:
```python
import unittest

def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mx, mn = max(lst), min(lst)
    return mx if mx == mn else mn + 1

class TestNextSmallest(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_second_example(self):
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_single_value_list(self):
        self.assertIsNone(next_smallest([1]))

    def test_equal_values(self):
        self.assertIsNone(next_smallest([1, 1, 1])) 

if __name__ == '__main__':
    unittest.main()
```
This code uses Python's `unittest` framework to automate the testing of the `next_smallest` function. The `TestNextSmallest` class derives from `unittest.TestCase`, allowing us to create test methods that start with the word 'test'. These methods enforce specific conditions using `self.assertEqual()` or `self.assertIsNone()`. 

The `unittest.main()` call runs the tests when the script is executed directly. For each test method, the framework executes the `next_smallest()` function with the argument appended to the list and ensures that the result matches the expected output. 

To run this test suite, execute the Python script in your command line or save it as a `.py` file and run it using your Python interpreter.