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

This approach uses a set to keep track of seen integers. For every integer `x` in the list, the code checks if `x` or `-x` has been previously seen. If it has been seen twice, then we return `True`. Otherwise, we add `x` or `-x` to the seen set. This algorithm has a time complexity of O(n), where n is the length of the input list `l`.