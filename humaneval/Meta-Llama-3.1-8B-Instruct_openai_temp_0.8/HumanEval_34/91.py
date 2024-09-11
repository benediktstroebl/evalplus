```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script does the following:

1. It defines a function `unique` that takes a list as input.
2. Inside the function, it uses a `set` to remove duplicates from the list.
3. It sorts the resulting set and returns it.
4. It demonstrates the usage of the function with an example list.

Note: Using a `set` for this purpose is more efficient than trying to remove duplicates from the list using Python's list methods, because it avoids the overhead of comparing each element with every other element. However, it does change the order of the elements, so we need to sort the set afterwards to get the desired output.