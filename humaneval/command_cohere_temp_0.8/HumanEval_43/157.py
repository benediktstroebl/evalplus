```python
def pairs_sum_to_zero(l):
    # Count the number of non-zero values
    c = sum(1 for n in l if n)
    # Return true if there are an even number of non-zero values, and no two elements add up to zero
    return c == 0 or c % 2 == 1
```

This solution uses a simple counting mechanism to determine the list's parities. If there is an even number of non-zero values, and no two elements add up to zero, then there must be two values whose sum is zero. The counting logic is leveraged to directly answer the problem, without needing to consider pairs of elements separately.