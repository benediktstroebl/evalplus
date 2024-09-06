```python
from typing import List

def filter_integers(values:
    """

    results = []
    for value in values:
        if isinstance(value, (int, float)):
            results.append(value)
    else:
        print(f'[{value}] is not an integer')
    return results

# Test case 1
test_values = [1, 2, 3, 'abc', {}, [5])
assert filter_integers(test_values) == [1, 2, 3]

# Test case 2
test_data = [1, 2, 3, 'abc', {}]
test_values = [1, 2, 3, 'a', [1, 2, 3, 4]]
test_values = [item for item in test_data if isinstance(item, int)]
assert filter_integers(test_values) == [1, 2, 3]
```

The function `filter_integers` takes a list of values and returns a new list containing only the integers. This is filtering is using a simple case-by-case comparison to identify the integers.