```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
"""
    return any(sum(x) == 0 for x in l) and any(x in l == 0) != 0
```
Now you can call this function and test it with different inputs.