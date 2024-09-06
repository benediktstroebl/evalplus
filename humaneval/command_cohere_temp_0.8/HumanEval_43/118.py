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

This function examines each integer in the list and adds it to a set. If it encounters a second integer that sums to zero with a previously seen integer, it returns `True`. The set is used to ensure that the function only considers distinct pairs of elements that sum to zero. 

This approach provides a time complexity of `O(n^2)` where `n` is the length of the input list, but can be improved to `O(n)` with a slight modification.