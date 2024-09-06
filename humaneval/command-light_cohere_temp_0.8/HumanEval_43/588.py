```python
def pairs_sum_to_zero(lst):
    return any(x + y <= 0 for x, y in zip(lst, lst[1:]))

# Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```
The provided code defines a function `pairs_sum_to_zero` that determines whether every element in a list of pairs results in a sum less than or equal to zero. The test cases cover various scenarios to ensure the function correctly identifies pairs with sum-zero elements.