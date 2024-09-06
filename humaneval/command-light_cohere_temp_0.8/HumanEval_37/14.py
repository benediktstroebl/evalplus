```python
def sort_even(lst):
    even_set = set(lst[1::index:: int])
    return [x if x not in even_set else even_set.find(x) for x in lst]

# Test the function
test_list = [5, 6, 3, 4]
test_list_sorted = sort_even(test_list)
print(test_list_sorted)  # Expected output: [3, 6, 5, 4]
```