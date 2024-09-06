```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x % 2, x))

# Test the function with sample inputs
test_list = [1, 2, 3, 4, 5, 6]
result = sort_even(test_list)
assert result == [3, 4, 5, 6, 1, 2]
```