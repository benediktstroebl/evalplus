```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    :param list l: The list to be sorted
    :return: sorted list
    """
    l_even = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l_even.append(l[i])
    else:
        l_even.append(l[i])
    l_even = sorted(l_even)
    return l_even
```