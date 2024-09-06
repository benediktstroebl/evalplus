Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.counter` to achieve the goal in O(n):
```python
from collections import Counter
from itertools import accumulate

def pluck(arr):
    even_values = [i for i in accumulate( Counter(arr).values() ) if i % 2 == 0 ]
    smallest_even, idx = (min(even_values), even_values.index(min(even_values))) if even_values else None
    return [smallest_even, idx] if smallest_even is not None else []
```
The approach uses `Counter(arr).values()` to get all unique values in the array and then accumulates them in the queue to filter out the even values and find the smallest one. Lastly, the index of the smallest even value is retrieved using `even_values.index(min(even_values))`.