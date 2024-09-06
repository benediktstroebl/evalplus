```python
def pairs_sum_to_zero(l):
    """
    Checks if all pairs of elements in the list sum to zero.
    """
    Returns True if any two elements in l that sum to zero, and False otherwise.
    """
    return bool(sum(l[::2]))
```