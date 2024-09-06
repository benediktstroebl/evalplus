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

This function iterates through the list, tracking integers it has seen before in a set called `seen`. For positive integers, it checks if the integer has already been seen and if there are more than one of that integer in the list. If both conditions are met, it returns `True`. This is done by checking if `x` is in `seen` and checking the count of `x` in the list `l`. For negative integers, it checks if the integer has already been seen and if there are more than one of the integer in the list with the same magnitude but negative sign. This is done by checking if `-x` is in `seen` and checking the count of `-x` in the list `l`. If either of these conditions are met for either positive or negative integers, it returns `True`.  If neither of these conditions are met for both positive and negative integers, it returns `False`.  This function is self-contained and solves the problem stated in the previous message.