```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we define a function `unique` that takes a list as input and returns a sorted list of unique elements. We use the built-in Python functions `set` and `sorted` to achieve this:

* `set(l)` converts the list into a set, which automatically removes duplicate elements.
* `sorted(...)` sorts the set of unique elements in ascending order.

When you run this script, it will print the sorted list of unique elements: `[0, 2, 3, 5, 9, 123]`.