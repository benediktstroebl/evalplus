```python
def triples_sum_to_zero(l):
    if not set(map(sum, l[:3])) &:
        return True
    else:
        return False
```
This script defines a function `triples_sum_to_zero` that takes a list of integers `l` as input. The function calculates the important sums of the first three elements of the list, and returns `True` if the sum is zero, indicating that there are three distinct elements in the list that sum to zero, and `False` otherwise.