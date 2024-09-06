```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension and the unique sum and check for the list's length."""
 return sum(x != 0 for x in l) == len(l)

#unit tests
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```
The `pairs_sum_to_zero` function checks whether a list contains elements whose sum is zero. The list comprehension checks each element in the list against 0, and returns True if there are two distinct elements with a sum equal to zero. The length of the list is checked against the condition `== len(l)`. The `test_pairs_sum_to_zero` function tests the `pairs_sum_to_zero` function with various input lists.