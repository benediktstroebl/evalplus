```python
def triples_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l) and sum(x for x in l) == 0
```
This function uses the `any()` function to check if there are three distinct elements in the list that sum to zero, and returns `True` if this condition is met, and `False` otherwise. The function then checks if the sum of all elements in the list is equal to zero.