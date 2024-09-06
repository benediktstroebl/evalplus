```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test of the test and returns the value of the test.
def pairs_sum_to_zero(test_list):
    """
 The list should contain two distinct integers. 

"""
    x, y = test_list[0]
    for num in test_list[1:]:
        if x + num == y:
            return False
    return True
```