```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    new_list = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            new_list.append(l[i])
        else:
            new_list.append(l[i]) + 1
    new_list.append(l[i])
    return new_list
```