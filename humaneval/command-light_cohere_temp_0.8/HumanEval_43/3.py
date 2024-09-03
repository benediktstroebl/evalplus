```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test
test_cases = [
    [ [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7], [1]]
]

for tc in test_cases:
    assert pairs_sum_to_zero(tc) == False
```