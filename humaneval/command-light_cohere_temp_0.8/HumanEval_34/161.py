```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [-None, float('inf')] and seen.add(x)]
```
This script defines a `unique` function that takes a list `l` as an argument. It uses a` seen = set()` to keep track of the elements it has seen so far. Then, it iterates through the list and checks if the current element `x` is not in the set `seen` and is not `None` or `inf`, and adds it to the seen set. Finally, it returns the unique elements in the list that passed the test.