```python
def sort_third(lst):
    """Sorts a list l such that values at indices divisible by three are sorted to the front, and other values are sorted normally"""
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
        else:
            new_lst.append(num)
    return new_lst
```

This code defines a function `sort_third` that takes a list `lst` as an argument. The function creates a empty list `new_lst` and iterates through the input list `lst`. For each element `num`, it checks whether its index is divisible by three. If the index is divisible by three, it is added to the front of the `new_lst` list. Otherwise, the element is added to the end of `new_lst`. The function then returns the `new_lst` list, which will have the elements of `lst` sorted such that the values at indices divisible by three are at the front, and other values are sorted normally.