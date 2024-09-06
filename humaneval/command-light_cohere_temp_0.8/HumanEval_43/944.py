```python
def pairs_sum_to_zero(l):
    return sum([x for x in l if x != 0]) <= 0

# Test cases:
[1, 3, 5, 0]
[1, 3, -2, 1]
[1, 2, 3, 7]
[2, 4, -5, 3, 5, 7]
[1]

# Result: False
```