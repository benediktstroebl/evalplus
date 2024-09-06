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

This function iterates through the list `l` and uses a set `seen` to keep track of elements present in the list. For every positive integer `x`, it checks if `x` is in the set, and if so, it checks whether `x` appears in the list more than once. If either of these conditions is met, it returns `True`. This is because if an integer `x` appears more than once in the list, and both occurrences sum to zero, then it contributes to a pair that sums to zero. For negative integers `x`, it uses the same logic, but checks against `-x` in the set to account for pairs that sum to zero. The overall time complexity of this code is O(n^2) where n is the length of l, due to the nested iteration over the set and list.