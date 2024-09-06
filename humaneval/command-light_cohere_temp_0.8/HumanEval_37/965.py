```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x[0]), reverse=True)

# Test the function
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
assert result == [3, 6, 5, 4]
```