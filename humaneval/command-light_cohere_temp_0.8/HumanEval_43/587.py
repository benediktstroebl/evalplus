Here's the solution:

```python
def pairs_sum_to_zero(lst):
    return any(x+y > 0 and not(x,y) in lst for x,y in zip(lst))

# Test cases
test_pairs_sum_to_zero = [
    ([1, 3], False),
    ([1, 3, -2], False),
    ([1, 2, 3, 7], False),
    ( [], False),
    ([2, 4, -5], True),
    ([1], False)
]

for test_case in test_pairs_sum_to_zero:
    assert pairs_sum_to_zero(test_case[0]) == test_case[1]
```