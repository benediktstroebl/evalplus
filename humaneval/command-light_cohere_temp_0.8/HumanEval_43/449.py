```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    function returns a integral-sum of all elements in l, and checks if there are 
    two that add up to zero.
    """
Note that this function assumes that all elements in l are integers."""
    
    return sum(x for x in l) % 2 == 0
```