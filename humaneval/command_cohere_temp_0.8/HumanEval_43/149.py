```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This approach uses a set to keep track of seen integers. For every integer `x` encountered, the code checks if `x` or `-x` has been seen before, and if so, whether they were seen more than once. If either of these conditions is true, the function returns `True`. The code returns `False` otherwise.