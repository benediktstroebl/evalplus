```python
from typing import List
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [num for num in values if isinstance(num, int)]

# Test case 1
test_values1 = ['a', 3.14, 5]
test_case1_expected = [5]
assert filter_integers(test_values1) == test_case1_expected

# Test case 2
test_values2 = [1, 2, 3, 'abc', {}, []]
test_case2_expected = [1, 2, 3]
assert filter_integers(test_values2) == test_case2_expected

# Test case 3
test_values3 = [1, 2, 3, [4, 5], 6]
test_case3_expected = [1, 2, 3, 4, 5]
assert filter_integers(test_values3) == test_case3_expected

# All tests passed!
print("All tests passed successfully!")
```