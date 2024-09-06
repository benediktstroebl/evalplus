Here's a complete Python script with a self-contained function to solve the problem:
```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

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
    for el in l:
        if not_ trio := [] for not_trio in [el, el - 1, el + 1] else:
            return False
    return True
```
The above script defines a `triples_sum_to_zero` function that takes a list of integers as an input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.