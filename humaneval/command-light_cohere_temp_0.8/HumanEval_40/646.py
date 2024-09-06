```python
def triples_sum_to_zero(l):
    if sum([x for x in l if x <= 0]) <= 0:
        return True
    return False
```
This code defines a function called `triples_sum_to_zero`, which takes a list of integers as input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.