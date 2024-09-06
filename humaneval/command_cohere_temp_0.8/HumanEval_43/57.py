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

This function iterates through the list, tracking positive and negative occurrences of numbers in the `seen` set. If it encounters a positive number `x`, it checks if `x` has already appeared in the list and if so, it checks if there is another occurrence of `x` besides the current one. If both conditions are satisfied, the function returns `True` as these `x` values form a pair that sums up to zero. The function performs a similar check for negative numbers, using the `seen` set. If both conditions aren't satisfied for any pair in the list, it returns `False`.