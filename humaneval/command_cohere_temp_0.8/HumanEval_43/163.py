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

This function iterates through the list, tracking elements in a set (to avoid repeating combinations). For positive elements, it checks if the element has been seen before and if there are multiple occurrences of it in the list. For negative elements, it checks if `-element` has been seen before and if there are multiple occurrences of `-element` in the list. If either of these conditions is met for two distinct elements, it returns `True`. Otherwise, it returns `False`.