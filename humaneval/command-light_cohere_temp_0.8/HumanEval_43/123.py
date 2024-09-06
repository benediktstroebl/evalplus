```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test function for the pairs_sum_to_zero function
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == True
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The code defines a function `pairs_sum_to_zero` that checks if any pair of elements in the list sum to zero. The test_pairs_sum_to_zero function contains a series of test cases to verify the correctness of the `pairs_sum_to_zero` function.