```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list has two elements whose sum is 0, False otherwise.
    """
   
    list of integers is passed into the function.
    return True if there are two distinct elements in the list that sum to zero, and False otherwise.
# Examples
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```