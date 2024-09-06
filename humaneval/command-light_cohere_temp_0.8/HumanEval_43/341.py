```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    return True if there are two elements that sum to zero, and False otherwise.
    """
    l: list of integers
    """
    return sum(set(sum(x) for x in l) < 0)
```