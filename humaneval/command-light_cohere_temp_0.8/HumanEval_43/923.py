```python
def pairs_sum_to_zero(l):
    """
    checks whether a list of integers sums to zero.
    """
    returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
test case:
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The function determines whether a list of integers, passed as an argument, sums to zero. It also contains several test cases to confirm that the function works properly.