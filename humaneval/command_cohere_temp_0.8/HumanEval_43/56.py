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

This function examines every element in the list, tracking the elements it has seen so far using a set data structure. For positive elements x, it checks if x has been seen before and if there are more than one occurrences of x in the list. If both conditions are met, it returns True. This is also done for negative elements, with the condition checked for -x. If these conditions are met for both positive and negative elements, it returns True; otherwise, it returns False.