```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print("Values 1:", values1)
print("Filtered:", filter_integers(values1))

values3 = [1, 2, 3, 'abc', (), [None] ]

print("Values 3:", values3)
print("Filtered:", filter_integers(values3))
```