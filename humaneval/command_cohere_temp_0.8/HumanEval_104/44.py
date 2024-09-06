```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
```python
import unittest
class TestUniqueDigits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
    def test_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
    def test_empty_list(self):
        self.assertEqual(unique_digits([]), [])
    def test_single_element(self):
        self.assertEqual(unique_digits([1]), [1])
    def test_multiple_elements_with_even_digits(self):
        self.assertEqual(unique_digits([152, 1422, 323, 152, 1]), [1])
if __name__ == '__main__':
    unittest.main()
```