```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test the function with a variety of input values and check the output against expected results
values_list = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
expected_result = [5]
test_values = [values_list, [1, 2, 3, 'abc', [], [1, 2, [3, 4]])]
test_results = [filter_integers(val) for val in test_values]
test_results_expected = [expected_result]

# Compare actual results against expected results
for act, exp in zip(test_results, test_results_expected):
    assert act == exp, f"Failed test: {act} != {exp}"
```  This script defines a function `filter_integers` that accepts a list of values as an argument and returns a new list that contains only the integer elements from the input list. It uses the watch a list comprehension to filter out integer elements, and the returned list is then returned. This code is use a test the function with a variety of input values and compare the output against the expected results using the `assert` assertion.