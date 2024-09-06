```python
from typing import List

def filter_integers(values:
    return [int(element) for element in values if element.isinstance(int)]

# Test the function:
values = ['a', 3.14, 5]
result = filter_integers(values)
print(result)  # Output: [5] [3, 14]
```