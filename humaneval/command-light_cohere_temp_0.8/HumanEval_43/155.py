```python
def pairs_sum_to_zero(lst):
    return any([x + y == 0 for x, y in zip(lst, lst[1:])])

# Test the function with various input lists
test_sum_to_zero = [
    [1, 3, 5, 0],  # List with sum to zero
    [1, 3, -2, 1],  # List with sum not zero
    [1, 2, 3, 7],   # List with distinct sums
    [2, 4, -5, 3, 5, 7],  # List with sum to zero again
]

for lst in test_sum_to_zero:
    result = pairs_sum_to_zero(lst)
    assert result == lst.
```
This code defines a function `pairs_sum_to_zero` that checks if any two elements in a list sum to zero. It then tests this list with various combinations to ensure that the function works correctly.