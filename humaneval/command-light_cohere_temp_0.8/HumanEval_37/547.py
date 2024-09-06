```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x % 2)

# Test the function
test_list = [1, 2, 3, 5, 6, 3, 4]
result = sort_even(test_list)
assert result == [3, 6, 5, 4, 1, 2]
```