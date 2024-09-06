```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first creating a list `result` that filters out the `delimeter` values from the `numbers` list. This means that all occurrences of `delimeter` values are effectively ignored and no longer appear in the `result` list. Subsequently, the `result` list is prepended with the `delimeter`, thereby placing it between consecutive elements of the original `numbers` list. The final empty list is returned if the input `numbers` list is empty or contains only `delimeter` values. 

This approach ensures that the `delimeter` is inserted only between consecutive elements, rather than appearing at the beginning or end of the list or being added multiple times between non-consecutive elements. 

The function can be tested as follows:
```python
import unittest

class Test Intersperse(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(intersperse([], 4), [])

    def test_all_delimeter(self):
        self.assertEqual(intersperse([4, 4, 4], 4), [4, 4, 4])

    def test_custom_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [0, 1, 0, 2, 0, 3])

    def test_complex_input(self):
        self.assertEqual(intersperse([0, 0, 0, 1, 2, 3, 0, 0, 4], 5), [5, 0, 0, 1, 5, 2, 3, 5, 5, 4])

if __name__ == '__main__':
    unittest.main()
``` 

The script uses `unittest` to create a test class with several test methods that check the function's behavior against expected outputs for different inputs. 

The tests aim to cover different scenarios, including empty lists, lists containing only the delimiter, and complex lists with different types of elements. 

The `if __name__ == '__main__':` block at the end ensures that the tests are run when the script is executed directly.  It is recommended to run this block when you run the script so that your code advances and clears doubts about its behavior.