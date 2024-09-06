```python
def double_the_difference(lst):
    odd = [x for x in lst if x % 2 != 0 and x >= 0 and isinstance(x, int)]
    return sum(x * x for x in odd)
```
```python
import unittest

class TestDoubleTheDifference(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_example2(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_example3(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_example4(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

if __name__ == '__main__':
    unittest.main()
```

The function `double_the_difference` uses a list comprehension to filter out odd integers from the input list, squares each of them using a generator expression, and returns the sum of the squared odd integers. The unit tests, which correspond to the example use cases specified in the problem, are included in the code and utilized to ensure that the function behaves as anticipated. 

The test cases cover a variety of scenarios, including positive and negative odd numbers, zero, and empty input lists. The `unittest.main()` function is used to run the tests when the script is executed directly.