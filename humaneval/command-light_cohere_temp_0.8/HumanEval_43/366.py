```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# tests
test_pairs_sum_to_zero = [
    [ [1, 3], [1, -2], [2, 4, 3, 5], [1, 7], []]
]

test_pairs_sum_to_zero_ok = [
    [ [1, 3], [4, 12], [2, 2], [7, 0]]
]

test_pairs_sum_to_zero_fail = [
    [-2, 1],
    [0, 1],
    [2, 3, 5],
    [7, 7]
]

print(test_pairs_sum_to_zero)
print(test_pairs_sum_to_zero_ok)
print(test_pairs_sum_to_zero_fail)

# pass this function with the tests
```