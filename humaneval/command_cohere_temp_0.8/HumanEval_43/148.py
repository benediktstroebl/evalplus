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

This approach uses a set to keep track of seen numbers. For every number `x` in the list, we try to complement it to sum up to zero. e.g., If we have a list of `[-2, 5, 3]` we want to complement `5` to have a sum of zero, so we check if `-5` is in the set. If it is present more than once, it confirms the existence of two elements summing up to zero.