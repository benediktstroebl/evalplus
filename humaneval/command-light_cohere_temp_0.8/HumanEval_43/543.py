```python
def pairs_sum_to_zero(l):
    """
    Function to determine if a list of integers has sum to zero
    """
    return all(x+y <= 0 for x,y in zip(l,l[1:]))

# Unit tests
def test_pairsumtozero():
    """
    Tests the pairs_sum_to_zero function
    """
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The provided Python code defines a function called pairs_sum_to_zero that checks whether a list of integers has a sum to zero. It uses the the universal method that checks if the list elements are elements of pairs with the sum to zero. The function returns True if the result if there are two distinct elements in the list that sum to zero, and False otherwise. The test_pairsumzero function also contains a series of tests that validate the correctness of the pairs_sum_to_zero function.