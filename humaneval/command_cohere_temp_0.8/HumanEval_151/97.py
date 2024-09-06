```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_squares)
```
```python
import unittest

class TestDoubleTheDifference(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(double_the_difference([1]), 1)

    def test_list_with_multiple_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([-2, -1, 1, 3, 4, -4, 0, 0, 5, 0]), 81)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()
```

The function **double_the_difference** uses a list comprehension to filter out odd integers from the input list, squares each of them, and returns the sum of these squares. The **unittest** framework is used to organize test cases and run them when the script is executed directly. 

The test cases cover various scenarios, including a single number, lists with multiple numbers, and an empty list. The expected behavior is reflected in the test cases, ensuring the function's correctness. 

To execute the tests, make sure you have Python and the **unittest** module installed (usually included in the standard library). You can either save the code into a Python file (e.g., double_the_difference_test.py) and run it from the command line using `python double_the_difference_test.py` or use an integrated development environment (IDE) like PyCharm, Visual Studio Code, or Spyder to run the file directly.