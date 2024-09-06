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

This approach uses a set to keep track of seen integers. For every integer (`x`) encountered, the algorithm checks if `x` is in the set and if the list contains more than one occurrence of `x`. If both conditions are met, the algorithm returns `True`. The code also accounts for negative integers.