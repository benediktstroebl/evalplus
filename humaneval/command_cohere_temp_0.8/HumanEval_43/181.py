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

This function examines each integer x in the list l and adds x to the set seen if it has not been previously added. The function also adds -x to the set seen to check if the negative of x also exists in the list. If the condition l.count(x) > 1 or l.count(-x) > 1 is met, meaning that there are two distinct occurrences of x or -x, and they sum to zero, the function returns True. Otherwise, it returns False.