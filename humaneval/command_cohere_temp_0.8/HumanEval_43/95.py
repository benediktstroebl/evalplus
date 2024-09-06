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

This function iterates through the list `l` and flips the sign of each element (i.e., multiplies by -1). It then checks if the original element and its flipped counterpart have been seen before. If both are seen and each occurs more than once in the list, then return True. Otherwise, return False.