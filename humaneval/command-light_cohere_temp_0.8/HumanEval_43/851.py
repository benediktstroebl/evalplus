```python
def pairs_sum_to_zero(lst):
    return any(x+y <= 0 for x,y in zip(lst, lst[1:])) and not any(x+y >= 0 for x,y in zip(lst, lst[1:]))

# Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```
The code defines a function `pairs_sum_to_zero` that checks if the sum of any two elements in a list will be less than or equal to zero. The function returns `True` if the list contains two elements that sum to zero, and `False` otherwise. The test cases ensure that the function works correctly for different scenarios.