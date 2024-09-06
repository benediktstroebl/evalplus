```python
def pairs_sum_to_zero(l):
    """
    Checks whether all elements in the list sum to zero.
    """
    Returns True if two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    return False
    if l and len(set(l)) == 1 else
    True
    return

# Unit tests
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The provided code defines a Python function that checks whether all elements in a list sum to zero. The function uses the test whether the list has two distinct elements that sum to zero, and returns True, or else. It also contains a test suite that verifies the correctness of the pairs_sum_to_zero function with various inputs.