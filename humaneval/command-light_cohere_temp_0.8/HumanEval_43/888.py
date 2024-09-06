```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test function
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```
The provided code defines a Python function `pairs_sum_to_zero` that takes a list `l` of integers as input and checks whether there are two elements in the list whose sum equals zero. 

The function returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. 

The test function `test_pairsumtozero` is used to verify the correctness of the `pairs_sum_to_zero` function.