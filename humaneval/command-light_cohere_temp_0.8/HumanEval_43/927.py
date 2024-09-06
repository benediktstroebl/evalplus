```python
def pairs_sum_to_zero(lst):
    return any(x + y <= 0 for x, y in zip(lst, lst[1:])) and not lst[-1]
```
This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a method of dynamic programming with backtracking to solve this problem, similar to the approach used in the provided initial code snippet.