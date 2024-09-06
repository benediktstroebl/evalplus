```python
def pairs_sum_to_zero(lst):
    """
    Checks if there are two distinct elements in the list that sum to zero.
    Returns True if there are two elements that sum to zero and False otherwise.
    """
The sum of all pairs of elements in the list is calculated and compared to zero.
    """
If the sum is zero, it means there are no two elements that sum to zero, so the function returns True; otherwise, it returns False.

Example usage:
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
```