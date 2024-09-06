```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list has two distinct elements that sum to zero,
    False otherwise.
    """
    list of integers 
    """
    for i in range(len(l)):
        if l[i] > 0 and l[i] <= l[i-1]:
            return False
    return True
```