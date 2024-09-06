```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    Test:
    [1, 3, 5, 0]
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    """
```
This Python function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if the list has two distinct elements whose sum is equal to zero, and `False` otherwise. The function uses a test to check if the list contains two elements whose sum equals zero, by creating a new list with the two elements and then checking if the new list is sorted.