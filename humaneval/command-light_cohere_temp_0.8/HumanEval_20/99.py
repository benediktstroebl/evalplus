```python
from typing import List

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    min_value = float('inf')
    max_value = float('-inf')
    closest = [float('inf')] * 2
    for num in numbers:
        min_value = min(min_value, num)
        max_value = max(max_value, num)
        if max_value < closest[-1]:
            closest = [num] + closest
        closest = [num] + [max_value]
    closest = sorted(closest, reverse=True)
    return closest, min_value
```

The function `find_closest_elements` takes a list of numbers and sorts them in ascending order. It then iterates through the most extreme values (either the minimum or maximum) and removes them from the list. After iterating through the chain, it will have the largest and smallest numbers in the list, respectively. The function then returns the list of numbers in order and the corresponding minimum value.

For example, if the input list is `[1.0, 2.0, 3.0, 4.0, 5.0, 2], the0]
The function would return `[[2.0, 4.0], 2.0]` as theit previous test in the list, and the minimum value is 2.0.

The code is a concise and efficient way to solve the problem in Python.