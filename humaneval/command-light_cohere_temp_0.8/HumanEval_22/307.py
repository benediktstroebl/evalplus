```python
from typing import List

def filter_integers(values: 
    return [num for num in values if isinstance(num, int)]
):
    pass

# Test cases
values_test = [1, 2, 3, 'abc', [1, 2, 3], [123, '123']]

print(filter_integers(values_test))  # [1, 2, 3, 123]
```