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

This approach uses a set to keep track of seen integers. For every integer `x`, the code checks if `x` or `-x` has been previously seen. If both are seen, meaning there are two distinct elements that form a sum of zero, the function returns `True`. Otherwise, it adds `x` or `-x` to the set and repeats the process with the remaining items in the list.