```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    lst = len(l)
    for i in range(lst):
        if sum(l[:i]) == 0:
            return True
    return False
```