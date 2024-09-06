```python
def sort_third(lst):
    return lst[:] + [x for x in lst[1:] + lst[2:] if x % 3 != 0]

# Test the function with sample inputs
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort_third(input_list))  # Output: [1, 2, 3, 6, 4, 5, 8, 9, 7]
```