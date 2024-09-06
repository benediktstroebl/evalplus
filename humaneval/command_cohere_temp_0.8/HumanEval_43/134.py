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

This function examines each integer in the list and adds it to a set. For positive numbers, it checks if the integer already exists in the set and if there are more than one of these integers in the list; if so, it returns `True`. For negative numbers, it checks if `-x` already exists in the set and if there are more than one of these in the list, it returns `True`. If no such pair is found, it returns `False`.