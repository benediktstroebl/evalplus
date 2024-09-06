```python
def triples_sum_to_zero(l):
    """
    Returns True if there are three distinct elements in l such that their sum is 0,
    and False otherwise.
    """
    list of integers -> List comprehension and set difference are used to find the three distinct elements that sum to zero.
    """
return any([x for x in set(sum(l)) == 0])
```