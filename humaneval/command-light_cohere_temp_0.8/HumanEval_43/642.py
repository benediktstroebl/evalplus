```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

:param l: list of integers
:return: boolean indicating whether two elements sum to zero
"""
    if len(l) < 2:
        return False
    s = sum(l)
    return (s == 0)
```