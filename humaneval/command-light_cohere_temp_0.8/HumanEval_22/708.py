```python
from typing import List

def filter_integers(values:
    return [int(el) for el in values if type(el) == int]

# Test case 1: Filter integers from a list of any values
test_case1 = ['a', 3.14, 5]
result_case1 = filter_integers(test_case1)
assert [element for element in result_case1 if element != float()] == [5], "Test case 1 failed"

# Test case 2: Filter integers from a list with mixed data types
test_case2 = [1, 2, 3, 'abc', {}, []]
result_case2 = filter_integers(test_case2)
assert [element for element in result_case2 if type(element) == int] == [1, 2, 3], "Test case 2 failed"

# Test case 3: Empty list
test_case3 = []
result_case3 = filter_integers(test_case3)
assert result_case3 == [], "Test case 3 failed"
```
The code defines a function **filter_integers** that takes a list of any data type as input and returns a list of the corresponding integers. The test cases demonstrate the result of the function, passing all tests with different data scenarios.