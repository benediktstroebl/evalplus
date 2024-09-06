```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The function `sort_even` takes a list as an argument and returns a list with the odd indices intact and the even indices sorted. To do this, the function creates two new lists: `even` and `odd`, which comprise the even and odd indices of the original list, respectively. Subsequently, the function returns the original even indices concatenated with a sorted version of the original odd indices. This approach ensures that the original list is preserved in terms of odd indices, while the even indices undergo sorting based on their original values. 

Here is an example usage of the function:
```python
print(sort_even([1, 7, 3, 9, 2]))  # [1, 3, 2, 7, 9]
```

The function's behavior is illustrated by using this list. The resulting list is [1, 3, 2, 7, 9], where the odd indices (1, 3, 7, 9) are preserved and the even indices (2, 4) are sorted in ascending order.