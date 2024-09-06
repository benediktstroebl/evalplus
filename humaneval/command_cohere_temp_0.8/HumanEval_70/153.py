```python
def strange_sort_list(lst):
    # Optional: List of integers with no elements.
    if not lst:
        return []

    # Optional: Handling single element lists.
    if len(lst) == 1:
        return lst

    # Main algorithm, odd iterations sort by min, even iterations sort by max.
    result = [min(lst[0::2]), max(lst[1::2])]
    for i in range(1, len(lst) // 2 + 1):
        result.extend([min(lst[2*i:2*i+2]) if i % 2 else max(lst[2*i:2*i+2]) for _ in range(2)])
    if len(lst) % 2 == 1:
        result.append(min(lst[-1:]))
    return result
```

The algorithm leverages the fact that the list is always divided into even length chunks, with odd iteration sorting by minimum and even iteration sorting by maximum to sort the list in the desired 'strange' manner.