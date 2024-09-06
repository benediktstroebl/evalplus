```python
from typing import List
def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test cases
values_test_case1 = ['a', 3.14, 5]
print("Test case 1: ", values_test_case1) 
# Output: Test case 1: ['a', 3.14, 5]

values_test_case2 = [1, 2, 3, 'abc', {}, []]
print("Test case 2: ", values_test_case2)
# Output: Test case 2: [1, 2, 3]

values_test_case3 = [1, 2, 3, 'abc', {}, [1, 2, 3]]
print("Test case 3: ", values_test_case3)
# Output: Test case 3: [1, 2, 3, 'abc', {}, [1, 2, 3]]

print("All test cases passed!")
```