```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The function uses a list comprehension that iterates over each value in the input list values. The condition `isinstance(item, int)` checks if each item is an instance of the int class, which indicates that it is an integer value. If the condition is met, the item is included in the int_list. Finally, the function returns the int_list, which will contain only the integer values from the input list. 

Here is an example usage of the function and its test script:
```python
import unittest

from filter_integers import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        # Positive test cases
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([3, 9, -3, 0, 12.2, 14], [12.2, 14]), [3, 9, -3, 0])

        # Negative test cases
        self.assertEqual(filter_integers([1, 2, 'abc', [], {}]), [1, 2])
        self.assertEqual(filter_integers([0, None, [], ()], [None]), [0])

        # Edge case
        self.assertEqual(filter_integers([]), [])

    def test_filter_integers_empty_input(self):
        # Edge case where input list is empty
        self.assertEqual(filter_integers([]), [])

if __name__ == '__main__':
    unittest.main()
``` 

The test script consists of two test cases, one for positive test scenarios and one for negative test scenarios. In the positive test scenarios, the function is tested with input lists containing a mix of integer and non-integer values, expecting the function to return only the integer values. The negative test scenarios test the function with input lists containing only non-integer values or empty input lists, expecting the function to return an empty list. Finally, the `if __name__ == '__main__':` block is used to run the tests when the script is executed directly.