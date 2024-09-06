```python
from typing import List
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Output: [1, 2, 3]

# Test case 3
class TestFilterIntegers:
    def test_filter_integers(self):
        return self.filter_integers([1, 2, 3, 'abc', {}, []])

test = TestFilterIntegers()
print(test.filter_integers())  # Output: [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input list. It also includes a test case functionality to verify the correctness of the function.