```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    return False if any two elements sum up to a non-zero integer,
    otherwise return True
    """
    for i in range(1, len(l)):
        if l[i] > 0 and l[i - 1] > 0:
            return False
    return True
```