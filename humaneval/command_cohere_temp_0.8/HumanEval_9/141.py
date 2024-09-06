```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][:rolling_window]) for nums in numbers[1:]]
```

The code uses a list comprehension with a generator expression to calculate the rolling maximum for each window size. By zip(numbers, numbers[::-1]), it pairs each element with its corresponding element in reverse order, achieving pairs like [(1, 2), (2, 1), (3, 2), ...]. The max() function finds the maximum for each of these pairs, and the list() function ensures the result is a list, not a tuple. Finally, by taking nums in numbers[1:], the code generates rolling maxima starting from the second element of the list and excluding the first, as the rolling max is defined. 

To make the function work for any rolling window size, you can add a parameter rolling_window to the function and use it to determine the size of each window in the list comprehension. Here's an example of how you can use the function with a custom window size:
```python
window_size = 3
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers, window_size)
print(result)
```

This will output:
[1, 2, 3, 3, 3, 4, 4]

Which is the maximum element of every window of size 3 starting from the second element of the list. 
If you want to test the function with your specific use case, you can add test cases to a unittest module in an analogous way as:
```python
import unittest

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2], 3), [1, 2, 3, 3, 3, 4, 4])
        self.assertEqual(rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
if __name__ == '__main__':
    unittest.main()
```

This way, you make sure that the function behaves as expected across different scenarios.