```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    
    Args:
        values (List[Any]): A list of values that can be of any type.
    
    Returns:
        List[int]: A list of integers from the input list.
    
    Example:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
import unittest

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

This script defines the `filter_integers` function and includes test cases to ensure it works correctly. The function uses a list comprehension to filter out non-integer values from the input list. The `isinstance(value, int)` expression checks if a value is an integer. The script also includes a `main` block to run the test cases when the script is executed directly.