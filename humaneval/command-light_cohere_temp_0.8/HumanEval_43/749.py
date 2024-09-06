```python
def pairs_sum_to_zero(l):
    """
    Checks whether all elements in the list sum to zero.
    """
    if sum(l) == 0:
        return True
    else:
        return False
```
The provided code defines a Python function named pairs_sum_to_zero. It takes a another list of integers as input and determines whether all elements can be added to zero. The function returns True if the list elements are pairwise summable and False otherwise.