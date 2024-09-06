```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    return sum(x for x,y in zip(l[::2], l[1:])) == 0
```