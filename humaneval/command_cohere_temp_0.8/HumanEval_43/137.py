```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            complement = -i
        else:
            complement = i
        if complement in seen:
            return True
        seen.add(i)
    return False
```

This function iterates through the list, tracking elements in a set (to ensure the elements are unique). If the element is positive, it considers the complement to be `-element`. If the element is non-positive, it takes the complement to be `element`. If the complement is in the seen set, they form a pair that sums to zero, so it returns `True`. Otherwise, it returns `False`.