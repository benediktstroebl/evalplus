```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    function uses a optimized approach to find the triple
    """
    return sum(x for x in l if len(set(l)) < 3) == 0
```