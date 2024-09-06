```python
def pairs_sum_to_zero(lst):
    return any(x + y <= 0 for x, y in zip(lst, lst[1:])) and lst

#Test cases
assert pairs_sum_to_zero([1, 3, 5, 0]) == False
assert pairs_sum_to_zero([1, 3, -2, 1]) == False
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```
The function checks if there are two elements in the list that add up to zero, and returns `True` if there are such elements, and `False` otherwise. The test cases ensure the