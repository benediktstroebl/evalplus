```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list has two distinct elements that sum to zero, False otherwise.
    """
    return any([x, -x]) in l and -x in l != 0
```