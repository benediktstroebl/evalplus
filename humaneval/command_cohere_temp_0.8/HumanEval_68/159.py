Here's a Python script that solves the given problem with an efficient approach using `collections`:
```python
from collections import *

def pluck(arr):
    res, idx = None, None
    odds, evens = Counter(arr), Counter(filter(lambda x: x % 2 == 0, arr))
    
    if len(evens):
        res = min(k for k, v in sorted(evens.items()))
        idx = evens[res]
        return [res, idx] if idx < len(arr) else [res, -1]
    
    if len(odds):
        return [min(odds), idx_of_min(odds)]
    
    return []

def idx_of_min(counter):
    return min(range(len(counter)), key=lambda i: counter[i])
```

This approach utilizes the `Counter` class to efficiently count occurrences and find the minimum values. The odds and evens counters are separated to simplify the logic, and the index of the plucked node is found using the `idx_of_min` helper function.

Note: The given approach will return `-1` for the index if the min value is found more than once. This is due to the usage of the `idx_of_min` function, which returns the first index it finds with the minimum value. Adjustments can be made if you require a different behavior.  Feel free to ask if you'd like further clarification!