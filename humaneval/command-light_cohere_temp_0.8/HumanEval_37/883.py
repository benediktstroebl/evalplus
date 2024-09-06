```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Test the function
[5, 6, 3, 4] => sort_even([5, 6, 3, 4])
[3, 6, 5, 4]

# Test again
[1, 2, 3] => sort_even([5, 6, 3, 4])
[3, 2, 1, 4]
```