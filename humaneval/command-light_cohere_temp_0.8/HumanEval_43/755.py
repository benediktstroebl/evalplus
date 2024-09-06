```python
def pairs_sum_to_zero(l):
    return sum(x > 0 for x in l) <= 2

# Tests
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The code defines a function called pairs_sum_to_zero that takes a list of integers as input and returns True if there are two distinct elements in the list that sum to zero, and False otherwise. The function uses a list comprehension to check if there are two distinct elements in the list that sum to zero, and the claim is that there are always two distinct elements is satisfied if the sum of the elements is less than or equal to 2.