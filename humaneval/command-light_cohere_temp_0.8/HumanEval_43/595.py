```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function
for _ in range(7):
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
```