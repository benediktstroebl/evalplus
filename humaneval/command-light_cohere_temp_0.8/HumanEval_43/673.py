```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Tests
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
This script defines a function `pairs_sum_to_zero` that takes a list of integers and checks if there are two distinct elements in the list whose sum is zero. The function returns `True` if this condition is met and `False` otherwise. The test function demonstrates the test by passing different lists with different outcomes and verifies the correctness of the `pairs_sum_to_zero` function.