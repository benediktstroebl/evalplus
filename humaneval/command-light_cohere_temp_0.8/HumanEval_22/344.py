```python
from typing import List

def filter_integers(values:
    """
    return [int(el) for el in values if type(el) == int]
):
    pass

# Test
values = [1, 2, 'three', 3.14]
result = filter_integers(values)
assert len(result) == 4  # Validate length is correct
assert all(result == [1, 2, 3, 4])  # Validate results
```