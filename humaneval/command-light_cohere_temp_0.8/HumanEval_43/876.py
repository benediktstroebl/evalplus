```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension checks for two elements that add up to zero.

Returns: False
    """
    for x, y in l[::-1]:
        if x + y == 0:
            return False
    return True
```