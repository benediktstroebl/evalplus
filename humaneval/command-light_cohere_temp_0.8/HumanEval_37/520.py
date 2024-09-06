```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    new_list = []
    for index in range(len(l)):
        if index % 2 == 0:
            new_list.append(l[index])
    else:
        new_list.append(l[index])
        new_list.append(l[index])
    new_list.append(l[index])
    return new_list
```