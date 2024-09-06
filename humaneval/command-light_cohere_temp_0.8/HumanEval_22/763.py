```python
from typing import List
def filter_integers(values:
    """ Returns list of integers only """
    result = [x for x in values if isinstance(x, int)]
    return result

# Test case 1
test_values1 = [1, 2, 3, 'abc', {}, [5]]
test_result1 = filter_integers(test_values1)
assert [5] == test_result1, "Test case 1 failed"

# Test case 2
test_values2 = [1, 2, 3, 'a', [], [0, None, True])
test_result2 = filter_integers(test_values2)
assert [0, None, 1, 2, 3] == test_result2, "Test case 2 failed"

print("All tests passed!")
```