```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not set()]
    # this block is commented out as an alternative using set.if one_of to improve readability
    seen = set(lst)
    return lst
# uncommenting this block gives the same result as above
# return [x for x in set(lst) if x not in seen]
```