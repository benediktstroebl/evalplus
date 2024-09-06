```python
def triples_sum_to_zero(l: list):
    """
    Function to check if there are three distinct elements in a list that sum to zero.
    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    if sum(map(int, l)) == 0:
        return True
    return False
```