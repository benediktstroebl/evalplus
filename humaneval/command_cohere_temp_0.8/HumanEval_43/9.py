```python
def pairs_sum_to_zero(l):
    # iterate through all pairs
    for x, y in combinations(l, 2):
        if x + y == 0:
            return True
    return False
```

This function uses a basic iterative approach, it takes each pair of elements in the list and determines if their sum is equal to zero, and returns `True` if there are two distinct elements in the list that sum to zero. 

You can test this function by calling it with different lists and comparing the results with the provided tests. 
For example:
```python
pairs_sum_to_zero([1, 3, 5, 0])  # Output: False
pairs_sum_to_zero([1, 3, -2, 1])  # Output: False
pairs_sum_to_zero([1, 2, 3, 7])  # Output: False
pairs_sum_to_zero([2, 4, -5, 3, 5, 7])  # Output: True
pairs_sum_to_zero([1])  # Output: False
```