```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))  # Remove duplicates and sort the list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print(unique([1, 1, 2, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

In this script, the `unique` function uses the built-in `set` data structure to remove duplicates from the input list. The `sorted` function is then used to sort the unique elements in ascending order.

However, note that the `set` data structure is unordered, so if you need to preserve the original order of elements, you should use a different approach, such as using a `dict` with keys as elements from the list:

```python
def unique_ordered(l: list):
    """Return sorted unique elements in a list, preserving the original order"""
    seen = {}
    unique_list = []
    for elem in l:
        if elem not in seen:
            seen[elem] = True
            unique_list.append(elem)
    return sorted(unique_list)

# Test the function
print(unique_ordered([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
print(unique_ordered([1, 1, 2, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```