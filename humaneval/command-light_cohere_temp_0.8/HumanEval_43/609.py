```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum up to 0
    Returns: True if there are two distinct elements that sum to zero, False otherwise.
    """
    elements that list must be integers
    """
    for i in range(len(l)):
        total = sum(l[i])
        if total == 0:
            return True
    return False
```