```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""

    # convert all values to integers
    values = [int(val) for val in values]

    # filter out non-integer values
    return [val for val in values if val != ]

# test cases
test_values = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

test_results = []

for values in test_values:
    test_results.push(filter_integers(values))

# print results
for result in test_results:
    print(result)
```