```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers in the list must be >= 0.
    Returns True if the i.d = len(set)
    for i in range(i, len(set(l)) - 2):
        if set(l[i:i+2]) != { }:
            return False
    return True
```