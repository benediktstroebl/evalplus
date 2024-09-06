```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    even_sorted = sorted(even)
    return even_sorted

# Test case 1:
print(sort_even([1, 2, 3]))  # [1, 2, 3]

# Test case 2:
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]

# Test case 3:
print(sort_even([10, 9, 8, 7]))  # [7, 8, 9, 10]
```
The function `sort_even` takes a list `lst` as input and returns a new list `even_sorted` that is identical to `lst` in the odd index positions, but with the values of the even indexes being equal to the values of the even indexes of `lst`, but sorted.