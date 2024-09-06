```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test case function:
    test_list = [1, 3, 5, 0]
    assert pairs_sum_to_zero(test_list) == False
    test_list = [1, 3, -2, 1]
    assert pairs_sum_to_zero(test_list) == False
    test_list = [1, 2, 3, 7]
    assert pairs_sum_to_zero(test_list) == False
    test_list = [2, 4, -5, 3, 5, 7]
    assert pairs_sum_to_zero(test_list) == True
```