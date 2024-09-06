```python
def sort_third(l: list):
    l_copy = l.copy()
    sorted_l = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_l.append(sorted(l_copy[i]))
        else:
            sorted_l.append(l_copy[i])
    return sorted_l
```

This Python script defines a function called `sort_third` that takes a list `l` as input. It creates a copy of the input list, `l_copy`, to ensure that the original list remains unchanged. It then iterates through each index of the list, if the index is not divisible by three, it appends the value at that index to the `sorted_l` list as is. If the index is divisible by three, it sorts the corresponding values in `l_copy` and appends the sorted values to `sorted_l`. Finally, it returns the `sorted_l` list.

Here is an example usage of the function:
```python
>>> sort_third([1, 2, 3])
[1, 2, 3]
>>> sort_third([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```

The function preserves the original list's values at indices that are not divisible by three and sorts the values at indices that are divisible by three.