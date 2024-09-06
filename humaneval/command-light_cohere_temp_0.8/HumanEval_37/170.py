```python
def sort_even(lst):
    return lst[:] if len(lst)%2 == 0 else lst[:-]

# Test case 1
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]

# Test case 2
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]

# Test case 3
print(sort_even([7, 8, 9, 10, 1, 2, 3]))  # Expected output: [1, 2, 3, 7, 8, 9, 10]
```
The function `sort_even` takes a list `lst` as an argument and returns a new list `lst_even` that preserves the odd indices from the original list while making the values at the even indices equal to the values at the corresponding even indices of the original list.