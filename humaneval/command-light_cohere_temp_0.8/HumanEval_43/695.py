```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test case:
    test_list=[1, 3, 5, 0, -1, 7,2, 4, 6, 3, 5, -5, 3, -3, 5, -2, 7, -3, -5]
    if (sum(test_list) == 0):
        return True
    else:
        return False
```