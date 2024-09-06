```python
from typing import List

def filter_integers(values:
    """ Returns a list of integers from a list of any python values """
    result = [x for x in values if isinstance(x, int)]
    return result

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc'], [(), []]
test_results = [filter_integers(val) for val in test_values]

# Print results
print('Test Values:')
for value, expected_result in zip(test_values, test_results):
    print(f'{value}: {expected_result}', end=' ')
```