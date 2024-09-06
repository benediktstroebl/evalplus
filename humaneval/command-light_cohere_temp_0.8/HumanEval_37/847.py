```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x % 2 == 0) ^ x > 0)

# Test the function
list_to_sort = [5, 6, 3, 4]
result = sort_even(list_to_sort)
assert list_to_sort == result
```