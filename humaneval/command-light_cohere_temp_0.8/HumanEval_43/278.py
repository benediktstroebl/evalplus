```python
def pairs_sum_to_zero(l):
    """
    returns True if the list has two distinct elements that sum to zero, 
    and False otherwise.
    """
    function implements this test by two nested for loops, 
    and checks if the sum of two adjacent elements is zero, 
    then returns True, otherwise False.

""" Test suite
    test_suite = [
        [1, 3, 5, 0], 
        [1, 3, -2, 1], 
        [1, 2, 3, 7], 
        [2, 4, -5, 3, 5, 7], 
        [1]
    ]
    assert pairs_sum_to_zero(test_suite) == False
```