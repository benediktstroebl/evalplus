Here's a self-contained Python function that filters out integers from a list of various types:
```python
from typing import List

def filter_integers(values:
    # Filter only integers from the list
    integers = [x for x in values if isinstance(x, int)]
    return integers

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_results = filter_integers(test_values)

print(test_results)

# Input test case: ['a', 2, 3, 4, 5]
input_values = ['a', 2, 3, 4, 5]
input_results = filter_integers(input_values)

print(input_results)
```
This script has a self-contained function `filter_integers` that takes a list of values and returns a new list containing only the integers from that input. The test cases demonstrate how the value of this function. The output is the filtered integers from the test cases.