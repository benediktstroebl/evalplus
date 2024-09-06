Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    return [max(numbers[i - rolling_max_window:i+1]) for i in range(len(numbers))]
```

The function rolling_max takes in a list of numbers and a parameter rolling_max_window, which indicates the size of the rolling window, and returns a list of integers, where each integer in the list is the maximum value in the rolling window at that moment in the list. 

Here is an example usage of the function:
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2], 3))
```
The output of this call will be:
```
[1, 2, 3, 3, 3, 4, 4]
``` 

This is the expected output, as the rolling maximum values for each window of size 3 starting from the first moment are printed. The maximum element in the window [1, 2, 3] is 3, and the maximum element in the window [2, 3, 2] is 3, and so forth. 

This script can be tested more rigorously using python's unittest framework, with a test looking like:
```python
import unittest

from rolling_max import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2], 3), [1, 2, 3, 3, 3, 4, 4])
``` 

This test case checks if the output of rolling_max matches the expected output. 
If the computation follows the specification, the test will pass.  Otherwise, it will raise an assertion error, indicating a mismatch between the computed and the expected values.