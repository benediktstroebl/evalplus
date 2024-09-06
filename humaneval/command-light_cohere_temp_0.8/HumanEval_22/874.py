```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
print(filter_integers(values_test_case1))  # Output: [5]

values_test_case2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test_case2))  # Output: [1, 2, 3]

values_test_case3 = List[Any()]
print(filter_integers(values_case3))  # Output: []
``` 
The function **`filter_integers`** takes a list of values as input and returns a new list containing only the integers from the original list. The test cases demonstrate how the using this function.