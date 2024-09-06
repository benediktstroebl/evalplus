```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` from `number` itself, which yields the desired decimal part. 

Here is a simple test case to ensure this function behaves as intended:
```python
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(8.0), 0.0)
        self.assertEqual(truncate_number(0.12), 0.12)
if __name__ == '__main__':
    unittest.main()
```