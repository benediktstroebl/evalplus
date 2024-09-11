```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

However, the original problem requires a custom implementation of a function to achieve this, without using Python's built-in set data structure. If that's the case, here's an alternative solution:

```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    unique_elements = []
    for element in sorted(l):
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

In this custom solution, we first sort the list to ensure that duplicate elements are adjacent to each other. Then, we iterate over the sorted list and append each element to the `unique_elements` list only if it's not already present in the list. This way, we effectively remove duplicates while maintaining the original order.