```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
test_filter_integers = [
    [],
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

results = []
for test_data in test_filter_integers:
    results.append(filter_integers(test_data))

print("Test Cases:", results)
```