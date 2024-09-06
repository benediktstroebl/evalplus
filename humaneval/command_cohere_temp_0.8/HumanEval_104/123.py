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
    def test_several_elements_with_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 111, 4, 77, 1]), [1, 4, 15, 33, 77, 111])
    def test_elements_with_multiple_digits(self):
        self.assertEqual(unique_digits([12, 14, 224, 321, 1]), [1, 12, 14, 224, 321])
if __name__ == '__main__':
    unittest.main()
```