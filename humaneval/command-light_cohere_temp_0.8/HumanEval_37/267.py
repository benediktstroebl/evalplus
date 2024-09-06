```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    new_even = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            new_even.append(l[i])
    else:
        new_even.append(l[i])
    new_even.append(l[i])
    new_even = sorted(new_even)
    return new_even
```