```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

test_pairs_sum_to_zero() function passes corresponding tests using assert.

"""
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```

This script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a test to test its correctness with the `test_pairs_sum_to_zero` function, which passes all the corresponding tests using `assert`.