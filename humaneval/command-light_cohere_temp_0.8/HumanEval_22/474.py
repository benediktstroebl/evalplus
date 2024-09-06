```python
from typing import List

def filter_integers(values:
    """
    return [int(x) for x in values if type(x) == int]
):
    pass

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # Output: [5]
print(filter_integers(values2))  # Output: [1, 2, 3]
```