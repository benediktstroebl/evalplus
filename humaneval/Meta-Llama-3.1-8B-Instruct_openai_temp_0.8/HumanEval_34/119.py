```python
def unique(lst: list):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Example usage
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
    # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, removes duplicates using the `set` data structure, and returns the sorted result.

Here's how it works:

1. `set(lst)` creates a set from the input list, which automatically removes duplicates because sets only store unique elements.
2. `sorted(...)` sorts the set elements in ascending order.
3. The function `unique` returns the sorted set of unique elements.

The example usage at the end demonstrates how to use the `unique` function with a list. The output shows the sorted unique elements in the list.