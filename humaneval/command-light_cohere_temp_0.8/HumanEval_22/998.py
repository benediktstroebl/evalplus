```python
from typing import List
def filter_integers(values: 
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, 3, 'abc', 3.14, 5]
result = filter_integers(test_values)
print(result) # Output: [1, 2, 3, 5]
```