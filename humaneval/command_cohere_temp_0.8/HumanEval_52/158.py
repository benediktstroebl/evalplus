```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```
This would return the values of True and False, respectively, which conforms to the previously desired output. 

Let's add a suite of unit tests to fully validate the function:
```python
import unittest

class TestBelowThreshold(unittest.TestCase):
    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_false(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_below_threshold_with_single_value(self):
        self.assertTrue(below_threshold([7], 10))

    def test_below_threshold_with_empty_list(self):
        # Empty list should return True if threshold is not exceeded
        self.assertTrue(below_threshold([], 1000000))
        # Empty list should return False if threshold is exceeded
        self.assertFalse(below_threshold([], 0))

    def test_below_threshold_with_threshold_as_list_element(self):
        self.assertFalse(below_threshold([1, 2, 3, 10, 10], [10]))

if __name__ == '__main__':
    unittest.main()
```
This test suite covers various scenarios, including edge cases, to ensure the `below_threshold` function behaves as expected.