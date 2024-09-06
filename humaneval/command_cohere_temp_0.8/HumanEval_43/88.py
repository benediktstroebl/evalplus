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

This code solves the problem by iterating through the list of integers `l`. When it encounters a positive integer `x`, it checks if `x` occurs more than once in the list and if it's already encountered a negative integer `-x` that would sum up to zero with `x`. It uses a set `seen` to keep track of seen integers to avoid duplicates and fulfills the requirement of being a self-contained function by not relying on any external libraries.