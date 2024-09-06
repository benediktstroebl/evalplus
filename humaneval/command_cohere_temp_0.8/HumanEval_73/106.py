```python
def smallest_change(arr):
    ans = float('inf')
    for a in set(arr):
        cnt = arr.count(a)
        f, r = divmod(cnt, 2)
        ans = min(ans, f + r)
    return ans
```

The function `smallest_change()` iterates through the unique elements in the input array, counting how many of each element is present. It then determines the minimum number of changes required to make the count of each element an even number, which is the minimum number of changes required to make the array palindromic. The code ignores any element count that is already even, as it requires 0 changes for such elements. The lowest even count of elements will yield the minimum steps needed to make the array palindromic.

Here is a unittest test module for the above function:
```python
import unittest

def smallest_change(arr):
    return float('inf') if arr == [] else len(set(arr)) // 2

class TestSmallestChange(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)

    def test_example_2(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_example_3(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_only_even_numbers(self):
        self.assertEqual(smallest_change([2, 4, 6, 8, 10]), 0)

    def test_only_odd_numbers(self):
        self.assertEqual(smallest_change([1, 3, 5, 7, 9]), 4)

    def test_mix_of_numbers(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3) 

if __name__ == '__main__':
    unittest.main()
```

This test suite uses the `unittest` module to validate the functionality of the `smallest_change()` function against multiple test cases. Each individual test is implemented as a method within the `TestSmallestChange class`, and the `unittest.main()` function executes the test methods when the script is run directly.