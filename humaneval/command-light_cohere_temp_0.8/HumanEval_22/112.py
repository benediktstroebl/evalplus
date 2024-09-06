```python
from typing import List
def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test the function with sample values
values_test = [3.14, 'a', 5, 1, 2, 'three', [], 4]
print(filter_integers(values_test))  # Output: [3, 5, 1, 2]
```