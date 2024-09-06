```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension:
    [x for x in l if sum(x) == 0]
    """
    return bool([x for x in l if sum(x) == 0])
```