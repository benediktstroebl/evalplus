```python
def triples_sum_to_zero(l: list):
    """
    Function that returns True if the list contains three distinct elements that sum to zero, and False otherwise.
    """
    return sum(set for set in l) <= 0
```