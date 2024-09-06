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

This function examines every possible pair in the list `l` and uses a set `seen` to keep track of integers that have been seen. The function returns `True` if it finds two distinct elements in the list that sum to zero. It returns `False` if no such pair is found. This algorithm has a time complexity of O(n^2) but that can be improved to O(n) with a hash set using `collections.Counter` and a more sophisticated approach for tracking the pairs.