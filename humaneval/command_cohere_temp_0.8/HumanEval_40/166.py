```python
def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        for j in l:
            if i != j and j - i in seen:
                return True
            seen.add(i)
    return False
```

This code uses a set, `seen`, to keep track of integers that have been encountered while looping through the list `l`. Iterating through each element in the list, it checks if the difference between the current integer and each previously seen integer is in the set. If it finds three distinct elements that sum up to zero, it returns `True`. Otherwise, it returns `False`.