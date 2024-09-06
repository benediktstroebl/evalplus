```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    Python list of integers does not have a built-in sum function, so we compute the sum manually:
    return any(x+y for x,y in zip(lst)) <= 0

We define a list of integers and pass it to the function. The function checks if there are two distinct elements in the list that sum to zero. If the sum of any two elements is less than or equal to zero, the function returns True. Otherwise, it returns False.

Example:
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
```