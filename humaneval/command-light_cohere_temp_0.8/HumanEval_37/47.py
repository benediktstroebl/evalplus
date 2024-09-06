```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test the function with various inputs
 assert sort_even([1, 2, 3]) == [1, 2, 3]
 assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
 assert sort_even([10, 15, 20]) == [10, 15, 20]
 assert sort_even([-2, -1, -5]) == [-1, -2, -5]
```