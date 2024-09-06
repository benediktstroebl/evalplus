```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    list comprehension has simple method:
    return any(x+y<0 for x,y in zip(l, l[1:]))
    """
    return any(x+y<0 for x,y in zip(l, l[1:]))
```