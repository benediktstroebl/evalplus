```python
from typing import List
def filter_integers(values:
    returns = [int for x in values if type(x) == int]
    return returns

# Test the function with different input values
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([None, 2, 3, 'a'])))   # []
```