```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
```
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    
    def test_unique_digits_multiple_elements(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1, 322]), [1, 15, 33, 322])

    def test_unique_digits_no_elements(self):
        self.assertEqual(unique_digits([]), [])

    def test_unique_digits_single_element(self):
        self.assertEqual(unique_digits([152]), [])

if __name__ == '__main__':
    unittest.main()
```