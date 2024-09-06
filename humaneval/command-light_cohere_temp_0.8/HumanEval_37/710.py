```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Test the function with a list of numbers
test_list = [1, 2, 3, 4, 5, 6]
result = sort_even(test_list)
assert result == [3, 4, 5, 6, 1, 2]

# Test the function with a list of strings
test_strings = ["a", "bb", "ccc", "aaa"]
result = sort_even(test_strings)
assert result == ["ccc", "aaa", "bb", "a"]
```