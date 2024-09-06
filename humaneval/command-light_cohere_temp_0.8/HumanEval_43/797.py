```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    set of numbers is usually arranged such way, with the smaller one first.
    """
    first, second:..."
    for x in l:
        for y in l:
            if x + y < 0:
                return False
    return True
```