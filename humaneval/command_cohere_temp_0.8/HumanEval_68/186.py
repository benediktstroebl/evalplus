Here's a Python script that solves the given problem with an efficient approach using python 3.9+'s sortedcontainers:
```python
from sortedcontainers import SortedSet

def pluck(arr):
    even, odd = SortedSet(), SortedSet()
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even.add(n)
        else:
            odd.add(n)
    
    if even:
        return [min(even), even.bisect_left(min(even))]
    elif odd:
        return [min(odd), odd.bisect_left(min(odd))]
    else:
        return []
```
The above code efficiently handles cases where there are many duplicate values with even complexity. It partitions the values into two SortedSets, even and odd, and then uses bisect_left to find the index of the earliest occurrence of the smallest value, as per the problem's criteria.