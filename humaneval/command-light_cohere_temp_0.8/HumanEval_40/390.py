```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst that sum to zero, 
    and False otherwise.
    """
    triple_sum = sum([x for x, y, z in lst])
    
    if triple_sum < 0:
        return True
    return False
```