```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum to zero, False otherwise.
    """
    sum(i for i in l) and all(sum(group) <= 0 for _, group in set(l)))
    return True
```