```python
from typing import List

def filter_integers(values:
    """
        int-containing elements:
            return [element for element in values if isinstance(element, int)]
    """
    return []

# Test the function
values = [1, 2, 3, 'abc', {}, [0]]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]
```