Here is a Python script that contains a self-contained function `pairs_sum_to_zero` which solves the problem you provided:

```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i in l:
        if (i == l[0]) or (i == l[-1]):
            return False
    return True
``` 

This function will return "True" if the list has two distinct elements whose sum is zero, and "False" otherwise.