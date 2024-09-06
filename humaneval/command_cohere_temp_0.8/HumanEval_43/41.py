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

This function examines every element in the list, tracking those that have been seen before using a set data structure. When encountering a positive integer `x`, the function checks if `x` has been seen before and not just once, as this would lead to an invalid pair (e.g., 3 and 3). If these conditions are met, it returns `True` because the element `x` has a negated counterpart that, when added to it, would sum to zero. This is repeated with the negative counterpart check for negative integers `x`.