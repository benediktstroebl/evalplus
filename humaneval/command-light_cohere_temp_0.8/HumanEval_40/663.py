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
    # set up variables
    # check if all elements are numbers
    if not all(isinstance(x, (int, float)) for x in l):
        return False

    # check if sum of elements is not equal to zero
    sum_ = sum(l)
    if sum == 0:
        return True

    # check if all elements are identical
    if sum in l:
        return False

    # if the list has three distinct elements that sum to zero, return True
    for x, y, z in zip(l, l[1:], l[2:]):
        if sum(x, y, z) == 0:
            return True

    return False
```