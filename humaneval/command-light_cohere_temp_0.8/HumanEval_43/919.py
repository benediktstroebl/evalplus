```python
def pairs_sum_to_zero(l):
    """
    Checks if there are two distinct elements in the list that sum to zero.
    Returns: True if they, else False
    """
    for i in range(len(l)):
        if sum(l[i:]) == 0:
            return True
    return False
```