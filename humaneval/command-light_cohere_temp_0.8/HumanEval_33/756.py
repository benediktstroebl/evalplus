```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""

    #dict of lists to keep track of values that are divisible by three
    d = {}
    for i in range(len(l)):
        if l[i] in d:
            d[l[i]] += 1
        else:
            d[l[i]] = 1

    # loop through each value that is divisible by three
    for i in d:
        l[i] = sorted(l)[d[i]]

    return l
```