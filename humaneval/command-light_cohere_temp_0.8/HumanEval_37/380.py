```python
def sort_even(lst):
    even_list = [item for item in lst if item % 2 == 0]
    even_sorted = sorted(even_list)
    return even_sorted

# Test the function
input_list = [5, 6, 3, 4, 2, 1]
result = sort_even(input_list)
assert result == [3, 6, 5, 4, 2]
result = sort_even([1, 2, 3])
assert result == [1, 2, 3]
result = sort_even([5, 6, 3, 4])
assert result == [3, 6, 5, 4]
```