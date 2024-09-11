```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we use the built-in `set` function to remove duplicates from the list and then pass it to `sorted` to arrange the elements in ascending order. The `set` function in Python automatically removes any duplicate elements because sets only store unique elements. 

Note that the `set` function does not preserve the order of elements. If you need to preserve the original order while still removing duplicates, you can use a different approach:

```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

However, the first approach is generally more efficient for large lists.