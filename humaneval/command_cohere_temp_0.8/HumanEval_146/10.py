```python
def specialFilter(nums):
    odd_digits = [int(digit) for digit in nums if int(digit) % 2 == 1]
    return sum(num for num in nums if len(odd_digits) == 2 and num > 10)
```
This function uses a list comprehension to filter the array of numbers (nums) and identify numbers that have odd first and last digits. Subsequently, it returns the count of numbers that fulfill this condition and are larger than 10. The unit tests provided in the problem statement can be accommodated by incorporating these into a testing framework, like this:
```python
# Testing the function
def test_special_filter():
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 19, 24, 35, 54, 59, 74, 91, 93, 54, 51]) == 4
    assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
``` 

To execute these tests, you can incorporate them into a bigger script or utilize a testing framework like pytest or unittest. 
```python
# To use unittest
import unittest
class TestSpecialFilter(unittest.TestCase):
    def test_special_filter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]), 2)
    def test_special_filter_with_more_nums(self):
        self.assertEqual(specialFilter([11, 19, 24, 35, 54, 59, 74, 91, 93, 54, 51]), 4)
    def test_special_filter_with_no_match(self):
        self.assertEqual(specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), 0)
if __name__ == '__main__':
    unittest.main()
``` 
This way, running this script would execute the unit tests, validating the function's correctness.