```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 for c in str(x))]
    return sorted(odd)
```
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_odd_numbers(self):
        self.assertEqual(unique_digits([51, 93, 305, 407]), [51, 93, 305, 407])

    def test_no_even_digits(self):
        self.assertEqual(unique_digits([15, 33, 19, 107]), [15, 33, 19, 107])

    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])

if __name__ == '__main__':
    unittest.main()
```

The code defines a function `unique_digits()` which takes a list of positive integers as input. It uses a list comprehension to filter out numbers that have any even digits, and then sorts the resulting list in increasing order. The `unittest` module is used to define a test class with several test cases, covering different scenarios such as positive examples, edge cases, and an empty list. The `unittest.main()` function is called to run all the test cases when the script is executed directly.