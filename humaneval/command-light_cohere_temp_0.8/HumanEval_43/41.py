```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    check_sum= sum(x) == 0 for x in set(l)
    return any(check_sum)
```