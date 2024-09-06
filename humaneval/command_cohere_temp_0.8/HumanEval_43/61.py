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

This function iterates through the list, tracking positive and negative occurrences of numbers in a set. When both occurrences of number and its negative are found and the count is more than one, the function returns True. Otherwise, it returns False. It is important to note that the idea behind this approach is simpler - it is an intuitive algorithm, unlike its complexity. Also, the complexity of O(n^2) can be a downside for larger inputs.