```python
from typing import List
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

#Test the function
values = [1, 2, 3, 'abc', {}, [1, 2, 3])
print(filter_integers(values))  # Output: [1, 2, 3]
```