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

This function examines every element in the list. If the element is positive, it checks if it has previously been seen in the set and if there are more than one occurrence of it in the list. If the element is negative, it checks if `-element` is already in the seen set and if there are more than one of these in the list. If either of these conditions are met for two distinct elements, it returns True, otherwise it returns False.