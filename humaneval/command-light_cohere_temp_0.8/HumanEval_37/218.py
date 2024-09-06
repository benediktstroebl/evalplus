```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test case 1
[1, 2, 3] = sort_even([1, 2, 3])
print("[1, 2, 3] = sort_even([1, 2, 3])")

# Test case 2
[5, 6, 3, 4] = sort_even([5, 6, 3, 4])
print("[5, 6, 3, 4] = sort_even([5, 6, 3, 4]))

# Test case 3
[2, 1, 3] = sort_even([2, 1, 3])
print("[2, 1, 3] = sort_even([2, 1, 3])")

# Test case 4
[4, 3, 2, 1] = sort_even([4, 3, 2, 1])
print("[4, 3, 2, 1] = sort_even([4, 3, 2, 1]))
```

The function `sort_even` takes a list `l` as input and returns a new list `l'` which is identical to the original list `l` in terms of odd indices, while its values at even indices are equal to the values of the even indices of `l`, but sorted.