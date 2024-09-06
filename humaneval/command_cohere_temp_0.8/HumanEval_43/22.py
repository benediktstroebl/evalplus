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

This function iterates through the list, tracking positive and negative occurrences of numbers in the `seen` set. If it encounters a positive number `x`, it checks if `x` has already appeared in the list (`l.count(x) > 1`) and if so, returns `True`. The function also checks if the negative of that number (`-x`) has appeared more than once in the list and if so, returns `True`. If neither of these conditions are met, it moves on to the next number. If the function finishes without returning `True`, it returns `False` as the final answer. This solution has a time complexity of `O(n)` and is efficient for large lists.  This approach avoids multiple passes and uses a set to enhance performance for checking duplicates.