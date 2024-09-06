Here's a Python script that contains a function called unique_digits, which solves the problem you've described:
```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```

This function `unique_digits(xs)` takes a list of positive integers called `xs` as input and generates a new list. It iterates over each element `x` in the input list, checking if any digit in the string representation of `x` is even. If none of the digits are even, it includes `x` in the result list. Finally, it sorts the result list in ascending order and returns it.

The unit tests that come with this function should prove its correctness. You can use Python's built-in test framework, `unittest`, to run these tests:
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

    def test_single_element(self):
        self.assertEqual(unique_digits([1]), [1])

if __name__ == '__main__':
    unittest.main()
```

If you run this test script, the `unittest` framework will execute each test case and report whether the function's behavior matches the expected outcome.