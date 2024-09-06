```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    Python list comprehension is used to find the two elements that sum to zero.
    """
    if sum(x[i] for i, x in enumerate(l)) == 0:
        return True
    return False
```