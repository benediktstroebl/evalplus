```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```
```python
import unittest
class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    def test_unique_digits2(self):
        self.assertEqual(unique_digits([21, 41, 19, 34]), [21, 41, 19, 34])
    def test_unique_digits3(self):
        self.assertEqual(unique_digits([11, 2, 15, 33]), [11, 15, 33])
if __name__ == '__main__':
    unittest.main()
```