```python
def triples_sum_to_zero(lst):
    """
    Function to return True if the list has three distinct elements sum to zero, 
    False otherwise.
    """
    Returns a function that accepts a list lst as input and returns True if there 
    are three distinct elements in the list that sum to zero, and False otherwise.
    >>> triples_sum_to_zero([1, 3, 5, 0])
    True
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for el in lst:
        if not(sum([el for _ in range(3)]) == 0):
            return False
    return True
```