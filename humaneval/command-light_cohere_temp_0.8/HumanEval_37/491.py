```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

# Test the function
def test():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([-1, -2, -3]) == [-3, -2, -1]
    assert sort_even([10, 20, 30]) == [30, 20, 10]
```