Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.counter` to find the smallest even value and its index respectively:
```python
from itertools import accumulate, chain
from collections import Counter

def pluck(arr):
    even_values = list(chain.from_iterable(accumulate((x % 2 == 0 for x in arr), max)))
    indices = Counter(zip(even_values, arr)).most_common()[0][1][0] if even_values else []
    return [indices, min(indices)] if indices else []
```
The script utilizes Python's `itertools` and `collections` modules to efficiently identify the smallest even value and its index in the given array. It returns a list `[smallest_even_value, its_index]` or an empty list if no even values are present or the array is empty.