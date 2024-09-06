```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ```

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual('three one five')
        assert sort_numbers('three one five') == 'one three five'
        self.assertEqual('two three')
        assert sort_numbers('two three') == 'three two'
        self.assertEqual('six seven')
        assert sort_numbers('six seven') == 'six seven'
        self.assertEqual('zero one')
        assert sort_numbers('zero one') == 'zero one'

if __name__ == '__main__':
    unittest.main()
```

```

The code defines a function `sort_numbers` that takes a space-separated string of numbers as input and returns the sorted version of that string. The `numbers` list comprehension is used to convert the input string into a list of integers, and then the `sorted` function is used to sort the list in ascending order. The test suite consists of several test cases that verify the correctness of the `sort_numbers` function by passing different input strings and asserting that the output is correct.