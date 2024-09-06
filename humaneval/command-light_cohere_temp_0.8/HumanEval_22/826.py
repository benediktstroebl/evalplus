```python
from typing import List
def filter_integers(values: 
    return [x for x in values if type(x) == int]

# Test the function
test_filter_integers = [1, 2, 3, 'abc', [0, 'a'], []]
print(filter_integers(test_filter_integers))
```