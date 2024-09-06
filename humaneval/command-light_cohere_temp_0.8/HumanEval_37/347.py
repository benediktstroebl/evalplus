```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test cases
test_suite = [
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 20, 30]) == [10, 20, 30]
    assert sort_even([55, 66, 45, 80]) == [45, 66, 55, 80]
]
```