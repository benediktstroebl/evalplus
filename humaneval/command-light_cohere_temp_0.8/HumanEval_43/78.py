```python
def pairs_sum_to_zero(l):
    return any(x+y <= 0 for x,y in zip(l,l[1:]))

# Test the function with known results
test_cases = [
    [],  # [] => False
    [1],  # [1] => False
    [2, 4],  # [2, 4] => False
    [1, 3, -2, 1],  # [1, 3, -2, 1] => False
    [2, 4, -5, 3, 5, 7],  # [2, 4, -5, 3, 5, 7] => True
]

for case in test_cases:
    print(cases_sum_to_zero(case))
```

This function checks if any elements in the list sum up to zero, returning `True` if they do, and `False` otherwise.  It checks if the would list is empty or contains only one element, both of which are valid inputs.