Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.counter` to find the smallest even value and its index respectively:
```python
from typing import List
from itertools import accumulate
from collections import Counter

def pluck(arr: List[int]) -> List[int]:
    even_values = [x for x in accumulate(arr) if x % 2 == 0]
    if even_values:
        min_value, min_index = min(Counter(even_values).items()), even_values.index(min(even_values))
        return [min_value, min_index]
    else:
        return []
```
This approach handles the cases presented in the prompt efficiently. The `accumulate` function helps to filter even values from the array without the need for explicit loops. The `Counter` class is utilized to identify the index of the smallest even value. Overall, this solution is time and space efficient.