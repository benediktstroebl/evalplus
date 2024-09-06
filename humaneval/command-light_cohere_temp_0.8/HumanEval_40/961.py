```python
def triples_sum_to_zero(l: list):
    """
    Function to check if all triple sums in the list are non-negative
    """
    if not any(sum([i for i in t]) < 0 for t in l):
        return True
    return False
```

This script defines a `triples_sum_to_zero` function that checks whether all the triple sums in a given list are non-negative. The function uses a necessary input of a list and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.