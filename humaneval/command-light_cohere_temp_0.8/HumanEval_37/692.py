```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) if x.is_even(x) else x) if l else l)

def is_even(x):
    return x % 2 == 0

# Unit tests
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
assert sort_even([10, 11, 12]) == [10, 11, 12]
assert sort_even([15, 16, 17]) == [15, 16, 17]
```