```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

#Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', }, [{}, []]]
test_results = [filter_integers(value) for value in test_values]

print(test_results)
 ```