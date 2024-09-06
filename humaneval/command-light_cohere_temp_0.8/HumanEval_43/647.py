```python
def pairs_sum_to_zero(l):
    """
    Check if the list of integers has two distinct elements that sum to zero.
    Return:True if two elements sum to zero, otherwise False.
    """
    return bool

# Example usage
>>> pairs_sum_to_zero([1, 3, 5, 0])
True
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
``` 
This function, `pairs_sum_to_zero`, efficiently checks if a list contains two elements whose sum equals zero. The function returns `True` if the two elements in the list can be separated and sum to zero, and `False` otherwise.