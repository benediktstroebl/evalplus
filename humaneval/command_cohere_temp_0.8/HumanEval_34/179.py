```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This approach utilizes the `set` data type to efficiently keep track of unique elements as a dictionary would, but does so without the overhead of checking the keys of the dictionary. An element is added to the set with the `or` operator which allows for appending an element without raising a `TypeError` that would occur when trying to add an element that is already in the set using the `add` method. The function then sorts the returned unique elements in ascending order and yields a list of them.

Here is an example usage of the function with a more complex input:
```python
print(unique([2, 5, 0, 12, 3, 1, 12, 5, 4]))
```

The function accepts the following input and returns a list of sorted unique elements:
```bash
[0, 1, 2, 3, 4, 5, 12, 12]
```