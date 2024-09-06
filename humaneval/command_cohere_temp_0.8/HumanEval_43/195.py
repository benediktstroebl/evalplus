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

This function examines every element in the list. If the element is positive, it attempts to find another element in the list that can be added to it to sum up to zero. If the element is negative, it attempts to find another element in the list that can be added to it with a negative sign to sum up to zero. For each potential pair, it checks if the pair exists twice in the list (once without the negative sign, and once with it, for the positive case). If such a pair is found, the function returns True, otherwise, it returns False.