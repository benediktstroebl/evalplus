```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [i for i in values if isinstance(i, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', }, []]
test_results = filter_integers(test_values)

# Print the results
for value, result in zip(test_values, test_results):
    print(f"{value}: should be {', '.join(test_result)}")
    print(f"is: {result}")
```