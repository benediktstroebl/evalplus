```python
def triples_sum_to_zero(l):
    """
    A recursive function that returns True if there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    return sum(a + b + c for a, b, c in l) <= 0
```