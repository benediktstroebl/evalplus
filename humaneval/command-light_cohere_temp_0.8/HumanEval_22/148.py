```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers."""
    return [i for i in values if isinstance(i, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 1, 2]
values_bad = ['a', 3.14, 'five']
print("Good: ", values_good)  # [5, 3, 1, 2]
print("Bad: ", values_bad)  # []

if len(filter_integers(values_good)) != 2:
    raise ValueError("Good filter failed the test!")

if len(filter_integers(values_bad)) != 0:
    raise ValueError("Bad filter failed the test!")
```