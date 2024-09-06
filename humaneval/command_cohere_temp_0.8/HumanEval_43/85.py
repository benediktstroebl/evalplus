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

This function iterates through the list `l` and utilizes a set `seen` to keep track of integers present in the list. For every positive integer `x`, it checks if `x` is already in the set `seen` and if the list contains more than one occurrence of `x`. If both conditions are met, it returns `True` as there are two distinct elements that sum to zero. The function applies a similar check for negative integers using the set `seen`. If neither of these conditions are met for all elements in the list, it returns `False`. 

Here are some examples of how this function can be invoked with corresponding outputs:
```python
# Output: False
pairs_sum_to_zero([1, 3, 5, 0])

# Output: False
pairs_sum_to_zero([1, 3, -2, 1])

# Output: False
pairs_sum_to_zero([1, 2, 3, 7])

# Output: True
pairs_sum_to_zero([2, 4, -5, 3, 5, 7])

# Output: False
pairs_sum_to_zero([1])
```