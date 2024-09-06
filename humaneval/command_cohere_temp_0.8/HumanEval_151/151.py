```python
def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for n in nums:
        if isinstance(n, int) and n % 2 != 0 and n != 0:
            result += n ** 2
    return result
```

The function `double_the_difference` iterates through each number in the input list. It checks if each number is an integer, odd, and not equal to zero. If so, it adds the square of this number to the `result` variable. The function returns 0 if the input list is empty or the numbers are not valid.

Here is a test suite that can be used to validate the function:
```python
def test_odd_squares(self):
    self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
    self.assertEqual(double_the_difference([-1, -2, 0]), 0)
    self.assertEqual(double_the_difference([9, -2]), 81)
    self.assertEqual(double_the_difference([0]), 0)
    self.assertEqual(double_the_difference([]), 0)
``` 

To run the test, you can add the test suite into a test module and run the tests using a testing framework like `pytest`.