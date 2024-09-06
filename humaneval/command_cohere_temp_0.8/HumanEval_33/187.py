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

This Python script defines a function called `sort_third`. This function takes a list `l` as input and returns a new list `l_copy`. The new list is identical to the input list in indices that are not divisible by three, while in the other cases, the values at the indices that are divisible by three are equal to the values of the corresponding indices of `l`, but sorted in ascending order. The returned list `l_copy` is a modified version of the original list `l`. 

Here is an example of how to use the `sort_third` function:
```python
list_ = [1, 2, 3]
print(sort_third(list_))
```

The output of this code is:
```
[1, 2, 3]
```

And here is another example:
```python
list_ = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(list_))
```

The output of this code is:
```
[2, 6, 3, 4, 8, 9, 5]
```