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

This function examines each element in the list. If it is positive, it checks if it has previously been seen in the set and if there are more than one occurrence of it in the list. If it is negative, it checks if its absolute value has previously been seen in the set and if there are more than one occurrences of its absolute value in the list. The function returns True if any of these conditions are met, indicating the existence of two distinct elements in the list whose sum is zero. Otherwise, it returns False.