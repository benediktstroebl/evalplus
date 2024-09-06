```python
def pairs_sum_to_zero(l):
    """
    checks whether there are two distinct elements in the list that sum to zero
    Returns: True if there are two such elements and they are not both negative, False otherwise.
    """
    list of integers is passed in
    """
    for x in l:
        for y in l:
            if x + y == 0:
                return False
    return True
```