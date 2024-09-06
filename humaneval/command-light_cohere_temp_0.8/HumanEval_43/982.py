```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list has two distinct elements that sum to zero, 
    False otherwise.
    """
    function is designed to return True if the list has two unique elements whose sum is equal to zero, and False otherwise.
    >>> test_pairs_sum_to_zero([1, 3, 5, 0])  # Should return True
   """
    return sum([x for x in l]) == 0
```