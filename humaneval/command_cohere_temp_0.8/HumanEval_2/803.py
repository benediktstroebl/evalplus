```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer smaller than `number` (the integer part), from `number` itself, resulting in the residual decimal part of the original number. 

Here's the unit test block, which can be run to test the function:
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