```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    Input:
    l: list of integers.
    Output:
    True if there are three distinct elements that sum up to zero in the list, and False otherwise.

Example usage:
    >>> triples_sum_to_zero([1, 3, 5, 0])
    True
    >>> triples_sum_to_zero([1, 3, -2, 1])
    False
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
```
The above script defines a `triples_sum_to_zero` function that takes a list `l` of integers as input. It checks whether there are three distinct elements in the list that sum up to zero. The function returns `True` if this condition is met, and `False` otherwise.