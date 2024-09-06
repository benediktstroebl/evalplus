```python
def pairs_sum_to_zero(l):
    """
    Function to determine if all pairs of integers in the list sum to zero.
    :param l: list of integers
    :return: boolean indicating if there are two distinct elements in the list that sum to zero
    """
    return sum(x+y for x,y in zip(l)) == 0

#Tests
def test_pairs_sum_to_zero():
    """
    Test function
    """
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The provided code defines a function called pairs_sum_to_zero that checks if all the pairs of integers in a given list sum to zero. It does this by iterating through pairs of elements in the list and computing the sum of each pair. The test_pairs_sum_to_zero function tests the pairs_sum_to_zero function with different input lists, asserting that it returns the correct boolean values.