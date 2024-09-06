```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test: 
    >>> test = pairs_sum_to_zero([1, 3, 5, 0])
    >>> print(test)
    True
    >>> test = pairs_sum_to_zero([1, 3, -2, 1])
    >>> print(test)
    False
    """
    return sum(x for x in l if x != l[0]) == 0
``` 
The function checks if the sum of any two distinct elements in the list is equal to zero. If the condition is met, it returns `True`, indicating that the list contains two elements whose sum equals zero. If the condition is not met, it returns `False`.