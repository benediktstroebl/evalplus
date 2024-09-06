```python
from typing import List

def filter_integers(values: 
    return [x for x in values if type(x) == int]
):
    pass

# Test the function
values = [1, 2, 3, 'abc', {}]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]
```