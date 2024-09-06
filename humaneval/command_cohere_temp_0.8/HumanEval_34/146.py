```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function unique takes a list l as input and returns a list of unique elements from l, sorted in ascending order. The function uses a set seen to track elements already encountered, initialized with no elements. The function then iterates over the input list l, and for each element x, it checks if x is not in seen, adds x to seen, and adds x to the result list. The function returns the unique sorted result.

Here is an example usage of the unique function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
```
[0, 2, 3, 5, 9, 123]
```

The output is the list of unique elements sorted in ascending order.