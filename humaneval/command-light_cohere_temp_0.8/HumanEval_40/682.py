```python
def triples_sum_to_zero(l: list):
    """
    A utility function to check if a list of integers sums to zero.
    Returns True if the  three distinct elements in the list sum up to zero, 
    and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    sum = sum(l)
    if sum == 0:
        return True
    return False
```