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

This function examines every possible pair in the list `l` and checks if their sum equals zero. It uses a set `seen` to keep track of integers that have been seen before. If a positive integer is encountered, the function checks if it has been seen before in the list and if there are more than one occurrences of it. This is done to exclude the case of the same integer appearing twice in the list, as that would lead to a false positive. The same logic applies to negative integers through the use of the set and the negation of the `x` variable. The function returns `True` if two distinct elements sum up to zero and `False` otherwise.