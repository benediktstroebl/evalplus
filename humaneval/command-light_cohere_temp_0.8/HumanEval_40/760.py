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
    # Check if all triple sums are non-negative
    for i in range(3):
        if not_negative_sum(l) and i != 2:
            return False
    return True

def not_negative_sum(l: list):
    """
    returns True if there exists a triple with distinct elements that have a negative sum.
    """
    return any of the triple sums are negative
```