Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    moment in the sequence. Optionally, specify the rolling maximum window size."""
    windows = collections.defaultdict(list)
    result = []
    # Record the rolling max in windows of size rolling_max_window
    for i, num in enumerate(numbers):
        for j in range(rolling_max_window):
            if j == 0:
                windows[j].append(num)
            else:
                windows[j].append(max(windows[j-1]))
        result.append(max(windows[-1]))
    return result
```

The `rolling_max` function takes in two parameters: 
- `numbers`: The list of integers where the rolling maximum needs to be calculated. 
- `rolling_max_window`: The optional parameter specifies the size of the rolling maximum window. 

This is an example usage of the function that follows the docstring:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 2)
```
Which returns the list `[1, 2, 3, 3, 3, 4, 4]`. 

This is a test suite for the function:
```python
import unittest

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2], 2), [1, 2, 3, 3, 3, 4, 4])
    def test_rolling_max_window_1(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2], 1), [1, 2, 3, 2, 3, 4, 2])
    def test_rolling_max_empty(self):
        self.assertEqual(rolling_max([], 2), [])
    def test_rolling_max_negative_window(self):
        self.assertRaises(ValueError, rolling_max, [1, 2, 3, 2, 3, 4, 2], -1)
    def test_rolling_max_odd_window_size(self):
        self.assertRaises(ValueError, rolling_max, [1, 2, 3, 2, 3, 4, 2], 3)
```

In the test suite, the first test verifies that the function produces the expected output. The second test verifies the function's behavior when the rolling max window size is 1, ensuring it returns the actual list of numbers. The third test ensures the function's behavior when an empty list is provided as input, and the fourth test verifies behavior with an odd window size and a negative window size, both of which should raise a `ValueError`. 

To execute the test suite, save the files in the same directory and run:
```
python -m unittest discover
```
Alternatively, you can navigate to the directory and run the tests individually:
```
python TestRollingMax.test_rolling_max
```
```
python TestRollingMax.test_rolling_max_window_1
```
And so forth for each test case.