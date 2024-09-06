```python
def pairs_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Test function
def test_pairsumtozero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The code defines the function `pairs_sum_to_zero` which checks whether the list's elements sum to zero or not. It uses the the all sums to zero, which is then passed to the `any()` function to check if the condition is met. The test function uses the expected values to pass the test cases and verifies that the `pairs_sum_to_zero` function correctly identifies two numbers that add up to zero.