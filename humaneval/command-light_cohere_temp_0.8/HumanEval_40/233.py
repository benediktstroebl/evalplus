```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst such that their sum is zero, 
    and False otherwise.
    """
    triple_sum = sum([x for x, y, z in zip(lst, lst, lst) if x + y + z == 0])
    return triple_sum == 0
```