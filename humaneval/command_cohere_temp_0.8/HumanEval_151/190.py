```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 == 1 and x >= 0)
    return int(odd_squares)
```
```python
import unittest

class TestDoubleDifference(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(double_the_difference( [1]) , 1)

    def test_multiple_numbers(self):
        self.assertEqual(double_the_difference( [1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference( [9, -2]), 81)
        self.assertEqual(double_the_difference( [0]), 0)
        self.assertEqual(double_the_difference( []), 0)

    def test_only_negative_numbers(self):
        self.assertEqual(double_the_difference( [-1, -2, 0]), 0)

if __name__ == '__main__':
    unittest.main()
```

The function **double_the_difference** uses a list comprehension to filter out odd, non-negative integers from the input list and calculates the sum of their squares. The sum is then returned as an integer if there are any numbers in the list, or 0 if the list is empty after the filtering. 

The **TestDoubleDifference** class houses multiple test functions that validate the correctness of the **double_the_difference** function against a variety of input scenarios. 

The script employs **unittest** to execute the tests and the **assertEqual** method to verify that the expected outcome matches the output of the function for a given input. 

To run the test, this code must be saved in a file and launched through a Python interpreter. You may also use the unittest module to selectively run tests. For example, running `unittest test_only_negative_numbers` will only run the test_only_negative_numbers function.  This helps to focus on specific areas of the code when executing tests.  Overall, this code illustrates a well-structured and organized approach to tackling the problem and validating the solution.