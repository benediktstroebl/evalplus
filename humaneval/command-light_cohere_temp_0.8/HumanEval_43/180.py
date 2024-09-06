```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    note that 0 is treated as a distinct element!
    """
    return sum(x for x in l) == 0
```