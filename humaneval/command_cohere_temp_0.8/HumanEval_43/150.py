```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This approach uses a set to keep track of seen integers. For every integer `x`, we add `-x` to the set to avoid double counting the pairs that sum up to zero. For example, the list `[1, 2, 3, 7]` will not return `True` because despite having multiple 2's and 7's, they are not the first element of a pair that sums to zero.