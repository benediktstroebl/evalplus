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

This function iterates through the list, tracking integers it has encountered before. It checks if the integer is positive, then it's added to the seen set, and if it's negative, then its negation is added to the set. If any integer is in the seen set and appeared more than once in the list, the function returns True, otherwise, it returns False.