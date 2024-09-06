```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list contains two elements that sum to zero, 
    False otherwise.
    """
    returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers contains two elements that sum up to zero: 1 + 3 = 4, and 2 + 4 = 6, which are the only numbers that sum to zero in this list.

#Test cases:
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False 
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```