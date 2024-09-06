```python
def pairs_sum_to_zero(l):
    """
    Check whether a list of integers can be summed to zero
    Returns: boolean indicating whether a list can sum to zero
    """
    s = sum(l)
    return s == 0
```