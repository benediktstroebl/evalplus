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

This function iterates through the list, tracking positive and negative occurrences of numbers in the 'seen' set. If it encounters a positive number 'x', it checks if 'x' has been seen before and if there are multiple occurrences of 'x' in the list. Similarly, it checks for negative occurrences of numbers that sum to zero. If any such pairs are found, it returns True, otherwise, it returns False.