```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part of the decomposition described in the prompt). The resulting difference will be the fractional part, or 'decimals', as described in the prompt. 

To validate this solution, you can create a test case in the same file, beginning with the import of the `unittest` module:
```python
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(2.0), 0.0)
        self.assertEqual(truncate_number(1.1), 0.1)
        self.assertEqual(truncate_number(0.9), 0.0)
```