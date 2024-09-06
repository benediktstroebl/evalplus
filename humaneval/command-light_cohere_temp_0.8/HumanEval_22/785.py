```python
from typing import List

def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test cases for function
values_test = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', [], {}]
]

test_case_results = filter_integers(values_test)

print("Test Case Results:", test_case_results)
```