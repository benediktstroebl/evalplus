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

This function examines every element in the list, tracking the elements it has seen so far using a set data structure. When it encounters a positive integer `x`, it checks if `x` has been seen before in the set and if there are more than one occurrence of `x` in the list. If both conditions are met, it returns `True`. The function performs a similar check for negative integers, `−x`, to identify pairs that sum to zero. The overall time complexity of this code is O(n), where n is the number of elements in the input list.