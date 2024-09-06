```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    lists of length three that sum up to zero:
    [1, 3, -2]
    [2, 4, 6]
    [5, 0, -5]
    """
    return sum((x for x in l if len(set(x)) == 2 and x in [0, -x])) == 0
```