```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```
```python
import unittest
class TestUniqueDigits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
    def test_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    def test_odd_list(self):
        self.assertEqual(unique_digits([151, 251, 161, 263, 323]), [151, 161, 251, 263])
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])
if __name__ == '__main__':
    unittest.main()
```