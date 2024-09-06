```python
from typing import List

def filter_integers(values:
        return [x for x in values if isinstance(x, int)]

# Test the function
values_list = [3.14, 1, (5), 'abc', [],]
result = filter_integers(values_list)
print(result)  # Output: [3.14, 5, ]:> int
```