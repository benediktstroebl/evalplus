```python
def pairs_sum_to_zero(lst):
    return any([x + y == 0 for x, y in zip(lst, lst[1:])]) and any([x == y for x, y in zip(lst, lst[1:])])

# Test cases
assert pairs_sum_to_zero([1, 3, -2, 1]) == True
assert pairs_sum_to_zero([1, 2, 3, 7]) == False
assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
assert pairs_sum_to_zero([1]) == False
```

This Python code defines a function named pairs_sum_to_zero that aims to determine if there are elements in a list that their sum is equal to zero. The function utilizes a two separate conditions: the first checks if there exist any elements in the list whose sum equals zero, and the second condition verifies if there are any elements in the list that are equal. This function efficiently handles the