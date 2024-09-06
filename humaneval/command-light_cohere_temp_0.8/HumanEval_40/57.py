```python
def triples_sum_to_zero(l: list):
    """
    Function to check if there are three distinct elements in a list that sum to zero.
    >>> bool(triples_sum_to_zero([1, 3, -2, 1]))
    True
    >>> bool(triples_sum_to_zero([1, 2, 3, 7]))
    False
    >>> bool(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))
    True
    >>> bool(triples_sum_to_zero([1]))
    False
    """  
    if len(set(l)) != 3 or set(l) != {0}:
        return False
    return True
```