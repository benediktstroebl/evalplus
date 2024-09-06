```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    l = [1, 3, -2, 1]
    if sum(l) == 0:
        return True
    else:
        return False
```