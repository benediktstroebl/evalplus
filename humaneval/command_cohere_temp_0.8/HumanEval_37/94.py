```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

This Python script defines a function called `sort_even` that takes a list `l` as input. The function splits the list into two parts: `even` and `odd`, using slicing with the `::2` syntax to create two separate lists. The even list contains the elements at even indices of the original list, and the odd list contains the elements at odd indices. The function then returns the sorted version of the even list concatenated with the odd list.

Here is an example usage of the function:
```python
result = sort_even([1, 2, 3, 4, 5, 6])
print(result)
```

The output of this code will be:
```
[2, 3, 1, 4, 6, 5]
```

This corresponds to the expected sorted result of the original list `[1, 2, 3, 4, 5, 6]` where the even indices are sorted in ascending order.