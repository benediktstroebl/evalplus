Here's a Python script with a self-contained function that solves the problem you described:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test cases:
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
    sum_to_zero = []
    for x in l:
        if x in sum_to_zero:
            if x + sum_to_zero[0] < 0:
                return False
        sum_to_zero.append(x
    sum_to_zero.append(x sum_to_zero.append(x sum_to_zero.append(x sum_to_zero))
    return True
    return False
```
This script defines a function called `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.  The function tests by iterating through the list and checking if each element adds up to zero.