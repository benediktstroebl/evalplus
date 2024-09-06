```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    integer list l: list
    """
    for x, y in zip(l, l[1:]):
        if x + y == 0:
            return True
    return False
```