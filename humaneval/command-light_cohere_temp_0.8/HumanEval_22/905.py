```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [
    [3, 14, 'abc', 1, 2, 'a', [], 5],
    [1, 2, 3, 4, 5, 6],
    [True, False, True, 2, 'three', 3]

test_cases = [[values for values in test_values]  # List of lists of test values]

# Test function with each individual test case
for test_case in test_cases:
    actual_output = filter_integers(test_case)
    assert actual_output == [x for x in test_case if isinstance(x, int)], "Test case failed"

# All test cases passed!
print("All tests passed.")
```