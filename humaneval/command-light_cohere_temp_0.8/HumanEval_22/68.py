```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = []
    for val in values:
        if isinstance(val, int):
            filtered_ints.append(val)
    return filtered_ints

# Test cases
values1 = [1, 2, 3, 'abc', ]

values2 = [1, 2, 3, 'four', 'five',]

values3 = [True, False, 3, 4, 5]

filtered1 = filter_integers(values1)
filtered2 = filter_integers(values2)
filtered3 = filter_integers(values3)

print("Test 1: Result:", filtered1)
print()

print("Test 2: Result:", filtered2)
print()

print("Test 3: Result:", filtered3)
```