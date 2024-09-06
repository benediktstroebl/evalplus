```python
def pairs_sum_to_zero(lst):
    """
    Checks if all the elements in the list sum up to zero.
    Returns True if the result if the list has two distinct elements that sum to zero
    """
    return sum(x for x in lst if x != 0) == 0
```