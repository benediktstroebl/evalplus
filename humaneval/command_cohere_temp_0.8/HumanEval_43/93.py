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

This function examines every element in the list. If the element is positive, it attempts to find another element in the list that can be added to it to get a sum of zero. If the element is negative, it attempts to find another element in the list that can be added to it with a negative sign to get a sum of zero. If there is a second occurrence of any element that can produce a sum of zero with the current element, the function returns True. Otherwise, it returns False.