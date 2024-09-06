```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    return True if there are two elements in l that sum to zero and False otherwise.
    """

Example:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    True
    """
    return sum([x for x in l if x != l[-1] and x + l[-1] <= 0]) == 0
```
The function implements a simple solution where it iterates through the list and checks for each element if it's not the same as the last element and if it's greater than or equal to the last element then it adds up the last element. The solution ensures that there are no two elements in the list that sum to zero. 

Would you like help with anything else?