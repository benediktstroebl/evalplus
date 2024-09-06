```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Tests
test_pairs_sum_to_zero = [
    [ [1, 3], [-2, 1], [2, 4, 3, 7], [1] ],
    [True, False, False, False]
]

# Execution
result = pairs_sum_to_zero(test_pairs_sum_to_zero)
print(result)  # Output: True
```