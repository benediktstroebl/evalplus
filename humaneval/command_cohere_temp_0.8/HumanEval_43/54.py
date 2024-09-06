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

This function iterates through every element in the list and simply checks if the absolute value of the number is already in the set to check for the presence of a second element with the same absolute value but with the opposite sign. The function returns True if such a pair is found, and False otherwise. This algorithm has a time complexity of O(n), where n is the length of the input list `l`.