```python
def pairs_sum_to_zero(l):
    return any(x+y <= 0 for x,y in zip(l, l[1:]))

# Tests
test_func = lambda: pairs_sum_to_zero([1, 3, 5, 0])  # pass
test_func = lambda: pairs_sum_to_zero([1, 3, -2, 1])  # fail
test_func = lambda: pairs_sum_to_zero([1, 2, 3, 7])  # fail
test_func = lambda: pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) # pass
test_func = lambda: pairs_sum_to_zero([1])  # fail

print("All tests passed!")
```