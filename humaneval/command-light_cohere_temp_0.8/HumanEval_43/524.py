```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list comprehension:
    lst = [x for x in l if sum(x) == 0]
    if len(llst) != 0:
        return True
    return False
```