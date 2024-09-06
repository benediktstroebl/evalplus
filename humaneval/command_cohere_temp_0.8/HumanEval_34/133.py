```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This `unique` function solves the problem by using a set `seen` to keep track of unique elements encountered while iterating through the list `l`. Elements that have already been seen are skipped, ensuring only unique elements are added to the final list. The returned list is then sorted to ensure consistent output order.

Here's an example usage and its expected output:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) 
```
**Output:**
```
[0, 2, 3, 5, 9, 123]
``` 
You can further verify the function's behavior by testing with other cases.