```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) if x.is_even(x) else x) if isinstance(l, list) else l

def is_even(x):
    return x % 2 == 0

# Test cases
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
assert sort_even([9, 2, 4, 7]) == [2, 4, 9, 7]
```