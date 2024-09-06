```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test the function with a variety of inputs
values_test = [['a', 3.14, 5, (1, 2, 3), 'abc', {}, []]
result_test = filter_integers(values_test)

print(result_test)
```