```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test the function
values = [1, 2, 3, 'abc', {}, [0, True, None]]
result = filter_integers(values)
print(result)  # Expected output: [1, 2, 3]

# Test with invalid values
values_invalid = [1, 2, 'three', (])
result_invalid = filter_integers(values_invalid)
print(result_invalid)  # Expected output: []
```