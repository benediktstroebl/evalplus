```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return sorted(lst) if even_lst == even_lst else [even_lst, lst]

# Test case 1:
print("Test Case 1:")
sort_even([1, 2, 3])  # [1, 2, 3]

# Test case 2:
print("Test Case 2:")
sort_even([5, 6, 3, 4])  # [3, 6, 5, 4]

# Test case 3:
print("Test Case 3:")
sort_even([10, 2, 4, 8])  # [10, 8, 2, 4]
```

This script defines a function `sort_even` which takes a list as an argument and returns a new list. It filters out even items from the filters even numbers out of a list and returns the sorted list.