```python
def median(lst):
    """Return the median of the list lst.
    if len(lst) % 2 != 0:
        raise ValueError("List must have an even number of elements.")
    m1, m2 = lst[::2], lst[1::2]
    return (m1 + m2) / 2 if len(m1) == len(m2) else None

# Example usage
lst = [10, 20, 4, 6, 3, 1, 2, 5]
print(median(lst))  # Output: 5.0
```