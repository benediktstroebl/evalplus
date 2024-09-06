```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers
    :param values: list of any python object
    :return: list of integers
    """
    return [num for num in values if isinstance(num, int)]

# test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc'], [1, 2, 3], [{}, []]]
test_results = [filter_integers(val) for val in test_values]

print("Test Results:")
for res in test_results:
    print(res)
```