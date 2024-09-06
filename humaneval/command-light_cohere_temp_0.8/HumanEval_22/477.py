```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
test_values = ['a', 3.14, 5]
test_result = filter_integers(test_values)
assert test_result == [5], "Test case 1 failed: Expected [5], got {}".format(test_result)

# Test case 2
test_data = [1, 2, 3, 'abc', {}, []]
test_result = filter_integers(test_data)
assert test_result == [1, 2, 3], "Test case 2 failed: Expected [1, 2, 3], got {}".format(test_result)

# Test case 3
test_strings = ['string', 'abc', 123]
test_result = filter_integers(test_strings)
assert test_result == [], "Test case 3 failed: Expected [], got {}".format(test_result)

print("All tests passed!")
```