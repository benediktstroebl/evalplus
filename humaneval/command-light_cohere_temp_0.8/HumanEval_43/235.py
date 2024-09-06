```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    a list of numbers that have the property that their sum equals zero.
    For example: [1, 3, 5, 0] and [2, 4, -5, 3, 5, 7] pass the test and return True.
    """
test:
    assert pairs_sum_to_zero([1, 3, 5, 0]) == True
    assert pairs_sum_to_zero([1, 3, -2, 1]) == True
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The `pairs_sum_to_zero` function accepts a list of integers as input and returns `True` if the list has two distinct elements whose sum equals zero, and `False` otherwise. The tests included in the script to ensure the correctness of the function.