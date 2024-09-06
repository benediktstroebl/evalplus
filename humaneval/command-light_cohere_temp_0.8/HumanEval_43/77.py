```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of pairs (x, y) that add up to zero is: [(-5, 3), (-3, 2), (1, -8)].

    """
    for x, y in l:
        if x + y == 0:
            return True
    return False
```