```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    """
    # sort the list
    l = sorted(l)

    # find the first three elements that sum to zero
    for i in range(0, len(l), 3):
        if sum(l[i:i+3]) == 0:
            return True

    return False
```