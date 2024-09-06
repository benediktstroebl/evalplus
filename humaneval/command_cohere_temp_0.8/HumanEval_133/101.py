```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    rounded_lst = [round(x) for x in lst]
    return sum(x * x for x in rounded_lst)
```

This script defines a function `sum_squares` that takes in a list of numbers and squares each rounded element while rounding them to the nearest higher integer before doing so. 

To test this script, you can create a test file with varying inputs and match the output of the function with the expected output. Here's an example:
```python
import unittest

class TestSumSquaresFunction(unittest.TestCase):
    def test_sum_squares_example1(self):
        self.assertEqual(sum_squares([1,2,3]), 14)

    def test_sum_squares_example2(self):
        self.assertEqual(sum_squares([1,4,9]), 98)

    def test_sum_squares_example3(self):
        self.assertEqual(sum_squares([1,3,5,7]), 84)

    def test_sum_squares_example4(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)

    def test_sum_squares_example5(self):
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

if __name__ == '__main__':
    unittest.main()
```

In this example, the `unittest` module is used to define a test class with various test methods that check the function's output against expected values. 

Running the tests will output either a success message if all tests pass or a failure message if any test fails, indicating whether the function behaves as expected. 
If the output of any test case is different from the expected output, the framework will throw an error and provide you with the specifics of the test(s) that failed.  This helps in validating your code to ensure it runs as expected.