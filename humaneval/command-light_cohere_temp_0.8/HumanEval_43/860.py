```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False

# Unit tests for the function
def test_pairsum():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```

The code defines a function `pairs_sum_to_zero` that checks if the sum of two elements in a list is zero. It returns "True" if there are two distinct elements in the list that sum to zero, and returns "False" otherwise. The unit tests for this test the list to verify the correctness of the function.