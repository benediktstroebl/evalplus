```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases
test_values = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

test_cases = [
    {'values': test_values, 'expected': [filter_integers(test_values)],
]

for case in test_cases:
    print(case['expected']) == case['values'])
```