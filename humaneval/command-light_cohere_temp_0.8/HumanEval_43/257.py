```python
def pairs_sum_to_zero(l):
    """
    returns True if all elements in the list sum to zero, 
    otherwise False.
    """
    test cases:
    test_cases = [1, 3, 5, 0, -2, 1]
    assert pairs_sum_to_zero(test_cases) == False
    test_cases = [1, 2, 3, 7]
    assert pairs_sum_to_zero(test_cases) == False
    test_cases = [2, 4, -5, 3, 5, 7]
    assert pairs_sum_to_zero(test_cases) == True
```