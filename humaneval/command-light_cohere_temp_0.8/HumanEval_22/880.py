```python
from typing import List

def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]
)

# Test case 1
test_values = ['a', 3.14, 5]
test_result = filter_integers(test_values)
assert test_result == [5], "Test case 1 failed: Expected [5], got {}".format(test_result)

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
test_result = filter_integers(test_values)
assert test_result == [1, 2, 3], "Test case 2 failed: Expected [1, 2, 3], got {}".format(test_result)
```
This Python script defines a function called `filter_integers` that filters a list of values based on whether each element is an integer. The function uses the filters the integers by iterating through the list and checking the `isinstance` of each element. The test cases demonstrate the verification of the `filter_integers` function by passing a list of values and asserting that the resulting filtered list matches the expected result.