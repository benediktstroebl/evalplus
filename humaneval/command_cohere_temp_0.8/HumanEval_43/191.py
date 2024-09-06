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

This function iterates through the list `l` and uses a set `seen` to keep track of elements present in the list. For every positive integer `x`, it checks if `x` is already in the set, and if so, it checks whether there are more than one occurrences of `x` in the list. The same is done for negative integers, by tracking `-x`. If either of these conditions are fulfilled, the function returns `True`. Otherwise, it returns `False`.