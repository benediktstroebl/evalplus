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

This function iterates through the list `l` and uses a set `seen` to keep track of elements present in the list. For every positive `x`, the function checks if `x` is in `seen` and if there are more than one occurrences of `x` in the list. If both conditions are met, it returns `True`. This is also done for negative numbers by using `-x` in the set. The function returns `False` if no two elements adding up to zero are found. 

The function is designed to be self-contained and solve the problem as outlined in the original prompt. It can be executed directly in Python and can also be imported as a module in other Python files.