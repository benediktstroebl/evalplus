```python
def triples_sum_to_zero(l: list):
    """
    Function that returns True if there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    triple_sums = [x for x in l if sum([x]) == 0]
    if len(triple_sums) == 3:
        return True
    return False
```