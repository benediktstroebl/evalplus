```python
def triples_sum_to_zero(l: list):
    """
    Function that returns True if there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    list of integers l = [1, 3, 5, 0]
    return sum((x for x in l if x != 0)) == 0
```