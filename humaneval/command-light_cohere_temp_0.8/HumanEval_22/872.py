```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', None, [], {}]
test_cases = [
    values=[1, 2, 3],
    values=['abc', 0, '123'],
    values=[])

test_results = []
for values in test_cases:
    test_results.append(filter_integers(values))

print('Test Results:')
for result in test_results:
    print(result)
```