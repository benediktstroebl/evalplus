```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

# Example usage
test_list = [1, 2, 3, 5, 6, 4]
result = sort_even(test_list)
assert result == [1, 2, 3, 5, 4]
result = sort_even([5, 6, 3, 4])
assert result == [3, 6, 5, 4, 1]
```