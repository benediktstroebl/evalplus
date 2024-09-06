```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) % 3)

# Test case 1
assert sort_third([1, 2, 3]) == [1, 2, 3]

# Test case 2
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

# Test case 3
assert sort_third([11, 22, 33, 44]) == [11, 22, 33, 44]

# Test case 4
assert sort_third([55, 66, 77, 88]) == [55, 66, 77, 88]
```
The function `sort_third` sorts the list `lst` using the `key` argument of the `sorted` function. It sorts values for `x same number that is not divisible by three, while the values that are divisible by three are left as they are. The `key` function uses the same number for this purpose.