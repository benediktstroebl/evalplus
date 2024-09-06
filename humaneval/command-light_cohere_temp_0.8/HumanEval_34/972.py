```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not _hidden_null_]

def _hidden_null_: None

# Tests
unique([5, 3, 5, 2, 3, 3, 9, 0, None])  # This should pass -> [0, 2, 3, 5, 9, None]
unique([0, 2, 3, 5, None])   # This should pass -> [0, 2, 3, 5]
unique([])           # This should raise error
```
The function `unique` takes a list as input and returns a new list with the unique elements from the original list, using a Set to keep track of elements we've seen before. The second test uses a function `_hidden_null_` to create a variable that is set to `None` and prevents any instances of `None` from being considered unique.