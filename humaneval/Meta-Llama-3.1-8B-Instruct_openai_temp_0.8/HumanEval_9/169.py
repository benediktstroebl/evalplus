Here's a Python script that uses a simple approach to solve this problem:

```markdown
### Rolling Maximum Problem Solution

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[:i+1]) for i in range(len(numbers))]
```

### Testing

```python
import unittest

class TestRollingMax(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([5]), [5])

if __name__ == '__main__':
    unittest.main()
```

### Running the Test

You can run the test by executing the script. The test will ensure that the `rolling_max` function works correctly for different scenarios.

You can also run the function directly with a list of numbers to get the rolling maximum elements.
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```