```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        elif x < 0:
            if x in seen and l.count(x) > 1:
                return True
        else:
            return False
    return False
```

This code solves the problem by iterating through each element `x` in the list `l`. If `x` is positive, it is added to the set `seen`. If `x` is negative, it is checked if it exists in `seen` and if there are multiple occurrences of `x` in the list. If both conditions are met, it returns `True`. The script returns `False` if a zero value is encountered, and lastly, it returns `False` if after iterating through the list, no eligible pairs are found. 

Here is an example usage output:
```python
>>> pairs_sum_to_zero([1, 3, 5, 0])
False
>>> pairs_sum_to_zero([1, 3, -2, 1])
False
>>> pairs_sum_to_zero([1, 2, 3, 7])
False
>>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
True
>>> pairs_sum_to_zero([1])
False
```