```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): List containing any type of python values

    Returns:
        List[int]: List containing filtered integers
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

In the above script, the `filter_integers` function uses a list comprehension to iterate over the input list and includes only the values that are of type `int`. The `unittest` module is used to run test cases on this function. The `isinstance` function is used to check if a value is an instance of a particular class. In this case, it's used to check if a value is an integer.