```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x % 2 == 0) and x or (not x % 2))

# Test the function with a list of integers
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
assert result == [3, 6, 5, 4]

# Test the function with a list of strings
test_strings = ["a", "bb", "ccc", "acc"]
result = sort_even(test_strings)
assert result == ["ccc", "acc", "bb", "a"]
```